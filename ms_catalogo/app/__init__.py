import os

from app.config import config
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app() -> Flask:
    app_context = os.getenv("FLASK_CONTEXT")
    app = Flask(__name__)

    f = config.factory(app_context if app_context else 'development')
    app.config.from_object(f)
    db.init_app(app)

    return app