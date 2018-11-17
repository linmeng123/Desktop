from app.views import blue


def create_app():
    from flask import Flask

    app = Flask(__name__)

    app.register_blueprint(blueprint=blue)

    return app