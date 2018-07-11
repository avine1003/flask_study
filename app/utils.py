# -*- coding: utf-8 -*-
from app.ext import db

__author__ = "wuyou"
__date__ = "2018/7/11 17:45"

class BaseModel:
    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
            return True
        except:
            return False

    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
            return True
        except:
            return False
