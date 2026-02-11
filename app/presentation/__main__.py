from flask import Flask

from app.presentation import routes


def create_app() -> Flask:
    app = Flask(__name__)
    routes.register(app)
    return app
