from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# from flask.ext.session import Session
from flask_session import Session

from app.models import db
from app.views import blue


def create_app():
    app = Flask(__name__)

    app.register_blueprint(blueprint=blue)

    # 秘钥 【session】
    app.config['SECRET_KEY'] = '$%^&*()dfghjk123123j4567wfTYUI123123sdfadjhgpo.,/.'


    ## flask-session 【session持久化】
    # 配置
    app.config['SESSION_TYPE'] = 'redis'    # 前提必须得有redis，redis服务必须是启动!

    # 超时
    app.config['PERMANENT_SESSION_LIFETIME'] = 60

    # 存储在客户端的 key名称
    app.config['SESSION_COOKIE_NAME'] = 'userSession'

    # 初始化 方式一
    # Session(app)

    # 初始化 方式二
    sess = Session()
    sess.init_app(app)




    ## flask-sqlalchemy 【ORM】
    # 配置数据库
    # sqlite:///  相对路径
    # sqlite://// 绝对路径
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # 初始化
    # db = SQLAlchemy(app)
    db.init_app(app)


    return app
