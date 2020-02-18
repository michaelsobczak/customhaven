from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from ..models import *

app = Flask(__name__)

def setup_app():
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.config['SECRET_KEY'] = 'you dont know this'
    app.config['SQLALCHEMY_DATABASE_URI'] = get_sqlalchemy_uri()
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


setup_app()


db = SQLAlchemy(app, model_class=Base)

from . import views, api