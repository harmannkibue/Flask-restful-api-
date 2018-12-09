# app/__init__.py

from flask import Flask

# initialize the app
app = Flask(__name__, instance_relative_config=True)

# load the config views
app.config.from_object('config')

# load the views
from app import views