import os
from os import path
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
STATIC_FILES_DIR = path.join(ROOT_DIR, 'static')
STATIC_URL = '/static/'

# Server settings
CURRENT_HOST = '127.0.0.1'
CURRENT_PORT = 8005

# Template settings
TEMPLATE_DIR = os.path.join(ROOT_DIR, "templates/")

