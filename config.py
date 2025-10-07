import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode - configurable via environment variable
DEBUG = os.environ.get('DEBUG', 'True').lower() in ('true', '1', 't')

# Secret key for session management
# IMPORTANT: Set a strong SECRET_KEY in production via environment variable
SECRET_KEY = os.environ.get('SECRET_KEY', 'dev-secret-key-change-in-production')

# Upload directory configuration
IMAGE_UPLOADS = os.environ.get('IMAGE_UPLOADS', 'static/image')

# Model configuration
MODEL_PATH = os.environ.get('MODEL_PATH', 'SkinCancerClassificationModelFinal.h5')
IMG_WIDTH = int(os.environ.get('IMG_WIDTH', '28'))
IMG_HEIGHT = int(os.environ.get('IMG_HEIGHT', '28'))
BATCH_SIZE = int(os.environ.get('BATCH_SIZE', '10'))

# Server configuration
HOST = os.environ.get('HOST', '0.0.0.0')
PORT = int(os.environ.get('PORT', '2500'))

