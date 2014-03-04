#-----------Flask Config----------------
DEBUG = True
SECRET_KEY = 'b7614af64f2f1c6fce84408fd05c946c6426fcdd03b48b60'

#-----------DB Config----------------
MONGODB_SETTINGS = {
'DB':  'project',
'USERNAME': 'admin',
'PASSWORD': 'admin',
'HOST': 'ds027749.mongolab.com',
'PORT': 27749
}

#-----------Mail Config----------------
MAIL_SERVER = "smtp.gmail.com"
MAIL_PORT = 465
MAIL_USE_SSL = True
MAIL_USERNAME = 'support@redbrick.io'
MAIL_PASSWORD = 'redbricksinbahriatown321'

#-----------Flask-Secuirty-Configs----------------

SECURITY_REGISTERABLE = True
SECURITY_REGISTER_URL= '/register'

SECURITY_CHANGEABLE = True
SECURITY_CHANGE_URL = '/change-password'

SECURITY_PASSWORD_HASH = 'sha512_crypt'
SECURITY_PASSWORD_SALT = "randomsaltvaluehere"


SECURITY_CONFIRMABLE = True
SECURITY_RECOVERABLE = True
SECURITY_TRACKABLE = True

#Email-Context
SECURITY_EMAIL_SUBJECT_REGISTER = 'Welcome to CoinEast'
SECURITY_EMAIL_SUBJECT_PASSWORD_NOTICE = 'Your password has been reset'
SECURITY_EMAIL_SUBJECT_PASSWORD_RESET = 'Password reset instructions'
SECURITY_EMAIL_SUBJECT_PASSWORD_CHANGE_NOTICE = 'Your password has been changed'
SECURITY_EMAIL_SUBJECT_CONFIRM = 'Please confirm your email'

#SECURITY_LOGIN_USER_TEMPLATE = 'security/login.html'
#SECURITY_EMAIL_SENDER = 'no-reply@redbrick.com'

#Views/Urls
SECURITY_REGISTER_URL = '/register'
SECURITY_LOGIN_URL = '/login'
SECURITY_LOGOUT_URL = '/logout'
SECURITY_CHANGE_URL = '/change-password'
SECURITY_RESET_URL = '/reset'
SECURITY_CONFIRM_URL = '/confirm'
SECURITY_POST_LOGIN_VIEW = '/account'
SECURITY_POST_LOGOUT_VIEW = '/'
SECURITY_POST_REGISTER_VIEW = '/'
SECURITY_POST_CONFIRM_VIEW = '/view-instructions'
SECURITY_POST_RESET_VIEW = '/'
SECURITY_POST_CHANGE_VIEW = '/'
SECURITY_CONFIRM_ERROR_VIEW = None
SECURITY_UNAUTHORIZED_VIEW = None
