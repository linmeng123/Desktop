from flask_script import Manager

from app import create_app

app = create_app('develop')

# @app.route('/')
# def hello_world():
#     return 'Hello World!'

manage = Manager(app)
if __name__ == '__main__':
    manage.run()
