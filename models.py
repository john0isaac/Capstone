from sqlalchemy import Column, String, Integer, Boolean, ForeignKey, create_engine
from flask_sqlalchemy import SQLAlchemy
import os
import json

database_name = "capstone"
database_path = "postgresql://{}@{}/{}".format('postgres:davinchi2020','0.0.0.0:5432', database_name)

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


'''
Industries

'''


class Industries(db.Model):
    ___tablename__ = 'industries'

    id = Column(Integer, primary_key=True)
    industry = Column(String(120))
    person = db.relationship('Person', backref='industries', lazy='dynamic')

    def __init__(self, industry):
        self.industry = industry

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'industry': self.industry
        }


'''
Info

'''


class Person(db.Model):
    ___tablename__ = 'person'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    address = Column(String(120))
    city = Column(String(120))
    phone = Column(String(120))
    website = Column(String(500))
    facebook_link = Column(String(120))
    seeking_job = Column(Boolean, default=False)
    profile_image = Column(String(500))
    industry_id = Column(Integer, ForeignKey('industries.id'), nullable=False)

    def __init__(self, name, address, city, phone, website, facebook_link, seeking_job, profile_image, industry_id):
        self.name = name
        self.address = address
        self.city = city
        self.phone = phone
        self.website = website
        self.facebook_link = facebook_link
        self.seeking_job = seeking_job
        self.profile_image = profile_image
        self.industry_id = industry_id

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'address': self.address,
            'city': self.city,
            'phone': self.phone,
            'website': self.website,
            'facebook_line': self.facebook_link,
            'seeking_job': self.seeking_job,
            'profile_image': self.profile_image,
            'industry_id': self.industry_id
        }
