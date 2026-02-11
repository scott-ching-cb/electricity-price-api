from flask import Flask

from .price import price_blueprint


def register(app: Flask) -> None:
    app.register_blueprint(price_blueprint)
