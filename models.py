from sqlalchemy import Column, String, Integer, create_engine
from flask_sqlalchemy import SQLAlchemy
from app import app
import os
import json

database_name = "capstone"
database_path = "postgresql://{}/{}".format('postgres:davinchi2020@localhost:5432', database_name)

db = SQLAlchemy()

'''
    setup_db(app)
    binds a flask application and a SQLAlchemy service
'''
def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()

setup_db(app)
'''
Table
'''

class Table(db.Model):
    ___tablename__='table'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __init__(self, name):
        self.name = name

    def format(self):
        return {
            'id': self.id,
            'name': self.name
        }