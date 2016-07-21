from flask import Flask
import os
#from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config.from_object('config')
app.config.from_envvar('FLASKR_SETTINGS', silent=True)
#bootstrap = Bootstrap(app)

from app import views, database

