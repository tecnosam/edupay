from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config import TEST_MODE

from dotenv import load_dotenv

import os

load_dotenv()


flask_app = Flask(__name__)
flask_app.secret_key = b'sample'
flask_app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')
flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(flask_app)

import app.models

db.create_all()

from app.setup import setup_status_rows
setup_status_rows()

if TEST_MODE:
    from app.test import load_all

    load_all()

import app.resources

import app.views
