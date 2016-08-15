import os


CSRF_ENABLED = True
SECRET_KEY = 'ldsjfpdljafsafjosdoja3498ew'

#PATHS
ROOT_DIR = os.path.realpath(os.path.dirname(__file__))
DATABASE = os.path.join(ROOT_DIR, 'data', 'myblog.db')
UPLOAD_AUDIO = os.path.join(ROOT_DIR, 'data', 'audio')
UPLOAD_IMAGE = os.path.join(ROOT_DIR, 'data', 'img')

USERNAME = "admin"
PASSWORD = "admin"

DEBUG = True # set it to False on production
