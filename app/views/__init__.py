# -*- coding: utf-8 -*-
from app.views.UserView import blue


# 懒加载， 后初始化方式
def init_blueprint(app):
    app.register_blueprint(blueprint=blue)


@blue.route('/')
def hello():
    return "hello blue"
