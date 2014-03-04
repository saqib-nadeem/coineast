from flask.ext.security import UserMixin, RoleMixin

#from coineast_exchange.core import db
from coineast_exchange import app
from flask.ext.mongoengine import MongoEngine

db = MongoEngine(app)

class Role(db.Document, RoleMixin):
    name = db.StringField(max_length=80, unique=True)
    description = db.StringField(max_length=255)

class User(db.Document, UserMixin):
    email = db.StringField(max_length=255)
    password = db.StringField(max_length=255)
    first_name = db.StringField(max_length=255)
    last_name = db.StringField(max_length=255)  
    balance = db.IntField()  
    BTC = db.FloatField()
    active = db.BooleanField(default=True)
    confirmed_at = db.DateTimeField()
    view_instructions = db.BooleanField(default=False)
    last_login_at = db.DateTimeField()
    current_login_at = db.DateTimeField()
    last_login_ip = db.StringField()
    current_login_ip = db.StringField()
    login_count = db.IntField()    
    roles = db.ListField(db.ReferenceField(Role), default=[])	
