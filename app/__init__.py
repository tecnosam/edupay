from flask import Flask
from flask_sqlalchemy import SQLAlchemy


flask_app = Flask(__name__)
flask_app.secret_key = b'sample'
flask_app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(flask_app)

import app.models

db.create_all()

import app.resources

import app.views
