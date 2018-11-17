import uuid

from flask import Blueprint, render_template, request, g, session, redirect, url_for

from app.ext import cache, db
from app.models import User, Goods

blue = Blueprint('blue', __name__)

def init_blue(app):
    app.register_blueprint(blueprint=blue)



## 基本显示
# @blue.route('/')
# def index():
#
#     wheels = [
#         {'name':'阿卡丽1', 'img':'/static/img/Akali_Splash_0.jpg'},
#         {'name': '阿卡丽2', 'img': '/static/img/Akali_Splash_1.jpg'},
#         {'name': '阿卡丽3', 'img': '/static/img/Akali_Splash_2.jpg'},
#         {'name': '阿卡丽4', 'img': '/static/img/Akali_Splash_3.jpg'},
#         {'name': '阿卡丽5', 'img': '/static/img/Akali_Splash_4.jpg'},
#     ]
#
#     goodslist = Goods.query.all()
#
#     return render_template('index.html', title='首页', wheels=wheels, goodslist=goodslist)



## 基本显示 - 分页处理(手动操作)
# @blue.route('/')
# @blue.route('/<int:num>/<int:per>/')
# def index(num=1, per=6):
#     wheels = [
#         {'name':'阿卡丽1', 'img':'/static/img/Akali_Splash_0.jpg'},
#         {'name': '阿卡丽2', 'img': '/static/img/Akali_Splash_1.jpg'},
#         {'name': '阿卡丽3', 'img': '/static/img/Akali_Splash_2.jpg'},
#         {'name': '阿卡丽4', 'img': '/static/img/Akali_Splash_3.jpg'},
#         {'name': '阿卡丽5', 'img': '/static/img/Akali_Splash_4.jpg'},
#     ]
#
#
#     # num 第几页
#     # per 一页显示多少个
#     # 1: offset(6*0).limit(6)
#     # 2: offset(6*1).limit(6)
#     # 3: offset(6*2).limit(6)
#     # goodslist = Goods.query.all()
#     goodslist = Goods.query.offset((num-1)*per).limit(per)
#
#     return render_template('index.html', title='首页', wheels=wheels, goodslist=goodslist)



## 基本显示 - 分页处理(手动操作)
# @blue.route('/')
# @blue.route('/<int:num>/<int:per>/')
# def index(num=1, per=6):
#     wheels = [
#         {'name':'阿卡丽1', 'img':'/static/img/Akali_Splash_0.jpg'},
#         {'name': '阿卡丽2', 'img': '/static/img/Akali_Splash_1.jpg'},
#         {'name': '阿卡丽3', 'img': '/static/img/Akali_Splash_2.jpg'},
#         {'name': '阿卡丽4', 'img': '/static/img/Akali_Splash_3.jpg'},
#         {'name': '阿卡丽5', 'img': '/static/img/Akali_Splash_4.jpg'},
#     ]
#
#
#     # num 第几页
#     # per 一页显示多少个
#     # 1: offset(6*0).limit(6)
#     # 2: offset(6*1).limit(6)
#     # 3: offset(6*2).limit(6)
#
#     # page 第几页
#     # per_page 一页多少个
#     # paginate.iter_pages 假设1000页，返回列表
#     # 当前是90页: 1、2、None、88、89、90、91、92、93、94、95、None、999、1000
#     paginate = Goods.query.paginate(num, per)
#
#     return render_template('index1.html', title='首页', wheels=wheels, paginate=paginate)


## 基本显示 - 分页处理(系统)
@blue.route('/')
# @cache.cached(timeout=60)
def index():
    wheels = [
        {'name':'阿卡丽1', 'img':'/static/img/Akali_Splash_0.jpg'},
        {'name': '阿卡丽2', 'img': '/static/img/Akali_Splash_1.jpg'},
        {'name': '阿卡丽3', 'img': '/static/img/Akali_Splash_2.jpg'},
        {'name': '阿卡丽4', 'img': '/static/img/Akali_Splash_3.jpg'},
        {'name': '阿卡丽5', 'img': '/static/img/Akali_Splash_4.jpg'},
    ]

    # 获取token
    # token = session.get('token')
    # user = None
    # if token:
    #     user = User.query.filter(User.token == token).first()

    # 当前页
    page = int(request.args.get('page') or 1)
    per = 6

    # page 第几页
    # per_page 一页多少个
    # paginate.iter_pages 假设1000页，返回列表
    # 当前是90页: 1、2、None、88、89、90、91、92、93、94、95、None、999、1000
    paginate = Goods.query.paginate(page, per)

    return render_template('index2.html', title='首页', paginate=paginate, user=g.user, wheels=wheels)


## 钩子函数
# @blue.before_request
# def before():
#     # request.remote_addr   IP
#
#     key = 'ip:' + request.remote_addr
#
#     # 缓存中获取值
#     value = cache.get(key)
#
#     if value: # 存在
#         return '过分了啊!'
#     else:   # 不存在
#         cache.set(key, '我不是爬虫!', timeout=3)


### FLASK内置对象
# @blue.before_request
# def before():
#     g.ip = request.remote_addr
#     g.haha = '不服啊，你咬我啊？'
#
#
# @blue.route('/cart/')
# def cart():
#     print(g.haha)
#     return  '你的IP地址:%s' % g.ip




### 全局变量g  + 钩子函数  【状态保持的一些用户处理】
@blue.route('/register/', methods=['POST'])
def register():
    user = User()
    user.email = request.form.get('email')
    user.password = request.form.get('password')
    user.name = request.form.get('name')
    user.token = str(uuid.uuid5(uuid.uuid4(), user.email))

    db.session.add(user)
    db.session.commit()

    # 状态保持
    session['token'] = user.token

    return redirect(url_for('blue.index'))


@blue.route('/login/', methods=['POST'])
def login():
    email = request.form.get('email')
    password = request.form.get('password')

    users = User.query.filter(User.email == email).filter(User.password == password)
    if users.count():
        user = users.first()
        # 更新token
        user.token = str(uuid.uuid5(uuid.uuid4(), user.email))
        db.session.add(user)
        db.session.commit()
        # 状态保持
        session['token'] = user.token
        return redirect(url_for('blue.index'))
    else:
        return '登录失败'


@blue.route('/logout/')
def logout():
    session.pop('token')

    return redirect(url_for('blue.index'))


@blue.route('/home/')
def home():

    # token = session.get('token')
    # if token:
    #     user = User.query.filter(User.token == token).first()
    # else:
    #     user = None

    return render_template('home.html', user=g.user)


@blue.route('/cart/')
def cart():
    # token = session.get('token')
    # if token:
    #     user = User.query.filter(User.token == token).first()
    # else:
    #     user = None

    return render_template('cart.html',user=g.user)

@blue.route('/about/')
def about():
    return render_template('about.html', user=g.user)



@blue.before_request
def before():
    token = session.get('token')
    if token:
        user = User.query.filter(User.token == token).first()
    else:
        user = None

    g.user = user