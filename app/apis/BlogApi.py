from flask import request, g
from flask_restful import Resource, abort

from app.models import UserModel


# 用户登录验证
def login_required(fun):
    def f(*args, **kwargs):
        u_token = request.args.get('u_token')
        if u_token:
            users = UserModel.query.filter(UserModel.u_token.__eq__(u_token)).all()
            if users:
                return fun(*args, **kwargs)
            else:
                abort(401, message='用户状态失效')
        else:
            abort(401, message='用户未登录')

    return f


# 用户权限验证
def check_permission(permission):
    def check(fun):
        def f(*args, **kwargs):
            u_token = request.args.get('u_token')
            if u_token:
                users = UserModel.query.filter(UserModel.u_token.__eq__(u_token)).all()
                if users:
                    user = users[0]
                    if user.check_permission(permission):
                        g.user = user
                        return fun(*args, **kwargs)
                    else:
                        abort(403, message='权限不够')
                else:
                    abort(401, message='用户状态已失效')
            else:
                abort(401, message='用户未登录')

        return f

    return check


class BlogResource(Resource):
    @login_required
    def get(self):
        return {'msg': '这是你的一堆博客'}

    @check_permission
    def post(self):
        user = g.user
        print(user)
        return {'msg': '写文章....'}
