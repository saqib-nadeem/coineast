from coineast_exchange import app

from flask.ext.mongoengine import MongoEngine
from flask.ext.mail import Message, Mail
from flask.ext.security import Security, MongoEngineUserDatastore

from coineast_exchange.models import User, Role
from coineast_exchange.forms import ExtendedRegisterForm


# Create database connection object
db = MongoEngine(app)

# Create mail object
mail = Mail()
mail.init_app(app)

# Setup Flask-Security
user_datastore = MongoEngineUserDatastore(db, User, Role)
security = Security(app, user_datastore, confirm_register_form=ExtendedRegisterForm)

