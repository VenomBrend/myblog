from app import app
import os


CSRF_ENABLED = True
SECRET_KEY = 'ldsjfpdljafsafjosdoja3498ew'

DATABASE = os.path.join(app.root_path, 'data', 'myblog.db')
UPLOAD_AUDIO = os.path.join(app.root_path, 'data', 'audio')
UPLOAD_IMAGE = os.path.join(app.root_path, 'data', 'img')

USERNAME = "admin"
PASSWORD = "admin"

DEBUG = True # set it to False on production