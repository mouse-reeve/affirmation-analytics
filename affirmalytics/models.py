''' Analytics postgres models '''
from flask.ext.sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Analytics(db.Model):
    ''' site stats table '''
    __tablename__ = 'analytics'
