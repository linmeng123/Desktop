from app.ext import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100))
    password = db.Column(db.String(256))
    email = db.Column(db.String(50), unique=True)
    token = db.Column(db.String(256))

# 商品模型类
class Goods(db.Model):
    # 商品id，主键
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # 商品名称
    name = db.Column(db.String(20))
    # 商品图片
    icon = db.Column(db.String(255))
    # 商品价格
    price = db.Column(db.Integer)
    # 商品描述
    detail = db.Column(db.String(255))