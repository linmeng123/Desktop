import random
from flask import Blueprint, abort, render_template, request, redirect, url_for, session

from app import db
from app.models import User

blue = Blueprint('blue', __name__)

@blue.route('/')
def index():
    # 获取用户名 -- cookie
    # username = request.cookies.get('username', '游客')

    # 获取用户名 -- session
    username = session.get('username')

    return render_template('index.html', username=username)



######## 异常处理
@blue.route('/errortest/')
def errortest():
    # 手动抛出异常
    abort(404)

    return '异常处理'

# 异常处理
@blue.errorhandler(401)
def err401(exception):
    print(exception)
    return ' <h1>  401？不存在的 </h1> '

@blue.errorhandler(404)
def error404(exception):
    return ' <h1> 404是什么？ </h1> %s ' % exception



#### 会话技术
@blue.route('/login/', methods=['GET','POST'])
def login():
    if request.method == 'GET': # 获取页面
        return render_template('login.html')
    elif request.method == 'POST':  # 登录操作
        # 获取数据
        username = request.form.get('username')

        # 状态保持 --- cookie
        # response = ?
        # response = redirect(url_for('blue.index'))
        # response.set_cookie('username', username)

        # 状态保持 --- session
        response = redirect(url_for('blue.index'))
        session['username'] = username

        return response


@blue.route('/cart/')
def cart():
    # 获取 -- cookie
    # username = request.cookies.get('username', '游客')

    # 获取 -- session
    username = session.get('username')

    return render_template('cart.html', username=username)


@blue.route('/logout/')
def logout():
    # cookie
    # response = ?
    # response = redirect(url_for('blue.index'))
    # response.delete_cookie('username')

    # session 方式一
    # response = redirect(url_for('blue.index'))
    # response.delete_cookie('session')

    # session 方式二
    response = redirect(url_for('blue.index'))
    session.pop('username')

    return response




################# 模板
@blue.route('/home/')
def home():

    name1 = 'Atom'
    name2 = '张三'
    name3 = '李四'

    goodslist = [
        {'name':'女朋友', 'price':'10W+', 'num':3},
        {'name':'苹果笔记本', 'price':'10W+', 'num':1},
        {'name':'苹果平板', 'price':'1W+', 'num':1},
        {'name':'苹果手机', 'price':'1.5W+', 'num':4},
        {'name':'苹果手表', 'price':'1W+', 'num':1},
        {'name':'苹果MP3', 'price':'500+', 'num':100},
    ]

    return render_template('home.html', name1=name1, name2=name2, name3=name3, goodslist=goodslist)




################# 模型
@blue.route('/createall/')
def createall():
    db.create_all()

    return '创建数据库或表单成功'

@blue.route('/dropall/')
def dropall():
    db.drop_all()

    return '删除表单成功'

@blue.route('/adduser/')
def adduser():

    # 实例化对象
    user = User()
    user.username = '测试-' + str(random.randrange(10000))
    user.age = random.randrange(100)

    # 存入数据库
    db.session.add(user)
    db.session.commit()

    return '添加用户成功'


@blue.route('/showuser/')
def showuser():

    # 获取数据
    users = User.query.all()

    return render_template('showuser.html', users=users)