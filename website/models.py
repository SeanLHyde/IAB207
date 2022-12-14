from . import db
from datetime import datetime
from flask_login import UserMixin



#User Database which utilises id as its primary key
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(128), unique=True)
    password = db.Column(db.String(20))
    name = db.Column(db.String(30))

#Events database which utilises id as its primary key and has a relationship
#comments
class Events(db.Model):
    __tablename__ = 'events'
    id = db.Column(db.Integer, primary_key=True)
    eventname = db.Column(db.String(80))
    description = db.Column(db.String(200))
    location = db.Column(db.String(80))
    date = db.Column(db.String(30))
    ticketamount = db.Column(db.String(10))
    ticketprice = db.Column(db.String(10))
    status = db.Column(db.String(10))
    creatorname = db.Column(db.String(80))
    image = db.Column(db.String(400))
    comments = db.relationship('Comments')

#Comments database which utilises id as its primary key and events_id as its foreign key  
class Comments(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String(240))
    events_id = db.Column(db.Integer, db.ForeignKey('events.id'))