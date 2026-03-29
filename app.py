from flask import Flask, render_template, request
from rembg import remove
from PIL import Image
import io
import base64
import logging

# Configure logging for professional error tracking
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

def img_to_data_url(img, format='PNG'):
    """Convert a PIL Image to a base64 Data URL."""
    try:
        buf = io.BytesIO()
        img.save(buf, format=format)
        buf.seek(0)
        b64 = base64.b64encode(buf.read()).decode('utf-8')
        return f"data:image/{format.lower()};base64,{b64}"
    except Exception as e:
        logger.error(f"Error converting image to data URL: {e}")
        return None

@app.route('/', methods=['GET', 'POST'])
def index():
    original_img = None
    processed_img = None
    
    if request.method == 'POST':
        file = request.files.get('image')
        if file and file.filename != '':
            try:
                # Open the uploaded image
                img = Image.open(file.stream)
                img_format = img.format if img.format else 'PNG'
                
                # Convert original image for preview
                original_img = img_to_data_url(img, img_format)
                
                # Remove background
                logger.info(f"Processing image: {file.filename}...")
                out_img = remove(img)
                
                # Convert processed image to data url for the template
                processed_img = img_to_data_url(out_img, 'PNG')
                logger.info("Successfully processed background removal.")
            except Exception as e:
                logger.error(f"Failed to process the image: {e}")
                
    return render_template('index.html', original_img=original_img, processed_img=processed_img)

if __name__ == '__main__':
    app.run(debug=True)
