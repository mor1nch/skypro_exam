from flask import Flask
from flask_restx import Api

from default_config import Config
from setup_db import db, SQLAlchemy
from views.birthday import birthday_ns


def create_app(config_object: Config) -> Flask:
    """Creating app and initializing config"""
    app = Flask(__name__)
    app.config.from_object(config_object)
    register_extensions(app)
    return app


def register_extensions(app: Flask) -> None:
    """Api creation and namespace initialization"""
    db.init_app(app)
    api = Api(app)
    api.add_namespace(birthday_ns)
    create_data(app, db)


def create_data(app: Flask, db: SQLAlchemy) -> None:
    """Database creation"""
    with app.app_context():
        db.create_all()


app = create_app(Config())
app.debug = True

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80, debug=True)
