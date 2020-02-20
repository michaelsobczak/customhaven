from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_gridify import FlaskGridify
import os
from ..models import AbilityCard, get_sqlalchemy_uri, Base

app = Flask(__name__)

def setup_app():
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.config['SECRET_KEY'] = 'you dont know this'
    app.config['SQLALCHEMY_DATABASE_URI'] = get_sqlalchemy_uri()
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


setup_app()


db = SQLAlchemy(app, model_class=Base)
grid = FlaskGridify(app, db, '/grids')

grid.gridify(AbilityCard)

from . import views, api