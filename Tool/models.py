from Tool import db
from datetime import datetime

class Survey(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    email = db.Column(db.String(64),unique = True,index = True)
    gender = db.Column(db.String)

    media = db.Column(db.String)
    age_limit = db.Column(db.String)

    information = db.Column(db.String)
    friend_stranger = db.Column(db.String)
    policies = db.Column(db.String)
    victim = db.Column(db.String)
    government = db.Column(db.String)
    social_sites = db.Column(db.String)
    parents = db.Column(db.String)
    school = db.Column(db.String)
    opinion = db.Column(db.String)

    def __init__(self, email):
        self.email = email
