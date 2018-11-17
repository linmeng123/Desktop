import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

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
    SECRET_KEY = 'vhijesbnviuwehnviuwhnjeiov'



#开发环境
class DovelopConfig(BaseConfig):
    DEBUG = True
    DATABASE = {
        'db': 'mysql',
        'driver':'pymysql',
        'username':'root',
        'password':'password',
        'host':'127.0.0.1',
        'port':'3306',
        'dbname':'flask03'
    }
    SQLALCHEMY_DATABASE_URI = get_db_uri(DATABASE)


# 测试环境
class TestingConfig(BaseConfig):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:////' + os.path.join(BASE_DIR, 'testing.db')

# 演示环境
class StagingConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = 'sqlite:////' + os.path.join(BASE_DIR, 'staging.db')

# 线上环境
class ProductConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = 'sqlite:////' + os.path.join(BASE_DIR, 'product.db')







config = {
    'develop':DovelopConfig,
    'testing':TestingConfig,
    'staging':StagingConfig,
    'product':ProductConfig,
    'default':DovelopConfig

}



def init_app(app,env_name):
    app.config.from_object(config.get(env_name))
