from app import app
import os


CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

DATABASE = os.path.join(app.root_path, 'data/myblog.db')

USERNAME = "admin"
PASSWORD = "admin"

DEBUG = True # set it to False on production