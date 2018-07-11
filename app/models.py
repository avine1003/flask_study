# -*- coding: utf-8 -*-
from app.ext import db
from app.utils import BaseModel

PERMISSION_READ = 1
PERMISSION_WRITE = 2


class UserModel(BaseModel, db.Model):
    u_token = db.Column(db.String(128), nullable=True)
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    u_name = db.Column(db.String(16))
    u_password = db.Column(db.String(256))
    is_activate = db.Column(db.Boolean, default=False)
    u_permission = db.Column(db.Integer, default=0)

    # 权限设计  1, 2, 4, 8, 16,...

    def check_permission(self, permission):
        return self.u_permission & permission == permission
