# Background Remover AI

This is a simple web application that removes the background from images using AI. It is built with Python, Flask, and the powerful `rembg` library.

## Features

- Upload an image and instantly get a background-removed version.
- Preview both the original and processed images side-by-side.
- Simple, user-friendly web interface.
- Ready for deployment via Docker (especially suited for Hugging Face Spaces).

## Tech Stack

- **Backend:** Python, Flask, Gunicorn
- **AI Model:** `rembg` (U2-Net)
- **Image Processing:** Pillow (PIL)
- **Frontend:** HTML/CSS (Jinja2 Templates)

## Getting Started

### Prerequisites

- Python 3.10+
- pip (Python package installer)

### Local Setup

1. **Clone the repository** (if you haven't already):
   ```bash
   git clone https://github.com/gnvvs-2003/BG-Remover-AI.git
   cd BG-Remover-AI
   ```

2. **Create a virtual environment** (recommended):
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install the dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**:
   ```bash
   python app.py
   ```
   The application will start on `http://127.0.0.1:5000/`.

## Running with Docker

This project includes a Dockerfile, making it easy to containerize and deploy.

1. **Build the Docker image**:
   ```bash
   docker build -t bg-remover-ai .
   ```

2. **Run the Docker container**:
   ```bash
   docker run -p 7860:7860 bg-remover-ai
   ```
   The app will be accessible at `http://localhost:7860`.

## Deployment (Hugging Face Spaces)

This app is configured to be easily deployed on Hugging Face Spaces via a Docker space. The `Dockerfile` handles the installation of necessary system dependencies (`libgl1`, `libglib2.0-0`), sets up a non-root user, exposes port `7860`, and serves the app using Gunicorn.
