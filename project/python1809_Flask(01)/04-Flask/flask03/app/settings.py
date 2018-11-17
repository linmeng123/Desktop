import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


# URI拼接
def get_db_uri(database):
    db = database.get('db') or 'mysql'
    driver = database.get('driver') or 'pymysql'
    username = database.get('username') or 'root'
    password = database.get('password') or '123456'
    host = database.get('host') or '127.0.0.1'
    port = database.get('port') or '3306'
    dbname = database.get('dbname') or 'sz01'

    return '{}+{}://{}:{}@{}:{}/{}'.format(db,driver,username,password,host,port,dbname)

class BaseConfig(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = '$%^&*()345671231adFGHJBHJK,./'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopConfig(BaseConfig):
    DEBUG = True
    DATABASE = {
        'dbname': 'szpython18091116'
    }
    SQLALCHEMY_DATABASE_URI = get_db_uri(DATABASE)


config = {
    'develop': DevelopConfig,
    'default': DevelopConfig
}

def init_app(app, env_name):
    app.config.from_object(config.get(env_name))