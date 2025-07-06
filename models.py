from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from datetime import datetime

db = SQLAlchemy()

class User(db.Model,UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer,primary_key=True)
    UserName = db.Column(db.String(100),unique=True)
    email = db.Column(db.String(100),unique=True)
    password = db.Column(db.String(20))
    workouts = db.relationship('Workout',backref='author',lazy=True)
# the last line make relationship one to many between User and Workout tables 
# first parameter 'Workout' ==> table want make relation with it allow to return list of workouts of each user
# second parameter make reverse relation wish allow achieve to user owner of workouts 
# ex: we have object workout = Workout() ==> workout.author ==> for get owner (user) of workouts
# third parameter lazy=True <==> lazy='select' ==> allow to load the data only when we want access to it 
# ex: only when we print(user.workouts) load data 

#UserMixin ==> is class wish provide the default implementation to mdthods wish falsk_login expect its existence in User class
# and they are helpfull in our code ==>{is_authenticated,is_active,is_anonymous,get_id(),...}

class   Workout(db.Model):
    __tablename__ = 'workout'
    id = db.Column(db.Integer,primary_key=True)
    pushups = db.Column(db.Integer,nullable=False)
    date_posted = db.Column(db.Date,nullable=False,default=datetime.now)
    comment = db.Column(db.Text,nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)