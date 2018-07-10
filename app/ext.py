# -*- coding: utf-8 -*-
from flask_session import Session
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_caching import Cache

db = SQLAlchemy()
migrate = Migrate()
sess = Session()
cache = Cache(config={
    'CACHE_TYPE': 'redis'
})


def init_ext(app):
    db.init_app(app=app)
    migrate.init_app(app=app, db=db)
    sess.init_app(app=app)
    cache.init_app(app=app)
