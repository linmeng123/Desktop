from flask import Blueprint, render_template
from app.models import User
blue = Blueprint('blue',__name__)
def init_blue(app):
    app.register_blueprint(blueprint=blue)


@blue.route('/')
def index():
    return render_template('index.html',title='首页')