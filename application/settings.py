import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# Server settings
CURRENT_HOST = '127.0.0.1'
CURRENT_PORT = 8005

# Template settings
TEMPLATE_DIR = os.path.join(BASE_DIR, "templates/")

