FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install system dependencies
# libgl1 and libglib2.0-0 are required by rembg/OpenCV
RUN apt-get update && apt-get install -y \
    libgl1 \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Create a non-root user (Hugging Face Spaces requires this sometimes for security)
RUN useradd -m -u 1000 user
USER user
ENV HOME=/home/user \
    PATH=/home/user/.local/bin:$PATH

WORKDIR $HOME/app
# Copy the rest of the application code
COPY --chown=user . $HOME/app

# Pre-download the rembg u2net model during build step (optional but prevents slow first-load)
RUN python -c "from rembg import new_session; new_session('u2net')"

# Expose port (Hugging Face spaces usually look at 7860)
EXPOSE 7860

# Run the app 
CMD ["gunicorn", "-b", "0.0.0.0:7860", "app:app"]
