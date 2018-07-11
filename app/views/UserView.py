# -*- coding: utf-8 -*-
from time import sleep
from flask import Blueprint, request, render_template, session
from app.ext import cache
# from app.models import UserModel

blue = Blueprint('blue', __name__)


@blue.route('/users/all/', methods=['GET', 'POST', 'PUT'])
def users():
    if request.method == 'GET':
        return render_template('UserRegister.html')
    elif request.method == 'POST':
        username = request.form.get('username')
        session['username'] = username
        return '注册成功'
    elif request.method == 'PUT':
        username = session.get('username', 'not exist')
        return username


@blue.route('/index/')
@cache.cached(timeout=20)
def index():
    sleep(4)
    return 'hhhhhhhhhhhhhhh'

@blue.before_request
def before():
    print('请求前')


@blue.route('/request/')
def req():
    print('正在执行视图')
    return 'hello AOP'