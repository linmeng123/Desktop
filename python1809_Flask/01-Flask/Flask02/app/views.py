from flask import Blueprint, render_template, request, redirect, url_for, session

bp = Blueprint('blog',__name__)


@bp.route('/')
def index():
    username = session.get('username')
    return render_template('index.html',username=username)

@bp.route('/login/',methods=['GET','POST'])
def login():
    if request.method == 'GET':
      return render_template('login.html')
    elif request.method == 'POST':
      username = request.form.get('username')
      response = redirect(url_for('blog.index'))
      session['username'] = username

      return response


@bp.route('/logout/')
def logout():
    session.pop('username')
    return render_template('index.html')
