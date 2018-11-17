import os

BASE_DIR = os.path.dirname(os.path.join(__file__))
def get_db_uri(database):
    db = database.get('db') or 'mysql'
    drive = database.get('drive') or 'pymysql'
    username = database.get('username') or 'root'
    password = database.get('password') or 'password'
    host = database.get('host') or '127.0.0.1'
    port = database.get('port') or '3306'
    dbname = database.get('dbname') or 'mydb'
    return '{}+{}://{}:{}@{}:{}/{}'.format(db,drive,username,password,host,port,dbname)

class BaseConfig(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = 'fchew8ot74ty3hueiw2y39'
    SQLALCHEMY_TRACK_MODIFICATIONS = False



class DevelopConfig(BaseConfig):
    DEBUG = True
    DATABASE = {
        'dbname':'flask03'
    }
    SQLALCHEMY_DATABASE_URI = get_db_uri(DATABASE)



config = {
    'develop':DevelopConfig,
    'default':DevelopConfig
}


def init_app(app,env_name):
    app.config.from_object(config.get(env_name))

