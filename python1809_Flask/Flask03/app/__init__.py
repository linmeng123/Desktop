from flask import Flask

from app.settings import init_app
from app.views import blue





def create_app(env_name='default'):

   app = Flask(__name__)

   #配置
   init_app(app,env_name)

   #插件
    # init_ext()

   app.register_blueprint(blueprint=blue)


   return app