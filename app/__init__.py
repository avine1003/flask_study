# -*- coding: utf-8 -*-
from flask import Flask

from app.ext import init_ext
from app.settings import envs
from app.views import init_blueprint


def create_app():
    app = Flask(__name__)
    # 初始化flask配置
    app.config.from_object(envs.get('develop'))
    # 初始化 扩展库
    init_ext(app)
    # 初始化蓝图
    init_blueprint(app)
    return app
