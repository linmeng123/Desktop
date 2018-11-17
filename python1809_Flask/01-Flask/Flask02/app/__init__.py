from flask import Flask

from app import views


def create_app():
    app = Flask(__name__)

    #注册蓝图
    app.register_blueprint(views.bp)

    app.config['SECRET_KEY'] = 'afnjnslkjNEiow;ji3w2;39wofj;fjwf'

    return app