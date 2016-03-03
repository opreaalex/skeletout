# -*- coding: utf-8 -*-

DEBUG = True
SECRET_KEY = 'super-secret-key'

MONGODB_SETTINGS = {
    'DB': 'generositree',
    'port': 27017,
    'tz_aware': True
}
CELERY_BROKER_URL = 'amqp://guest@localhost//'

MAIL_DEFAULT_SENDER = 'example@localhost.home'
MAIL_SERVER = 'smtp.localhost.home'
MAIL_PORT = 25
MAIL_USE_TLS = True
MAIL_USERNAME = 'changeme'
MAIL_PASSWORD = 'changeme'

SECURITY_POST_LOGIN_VIEW = '/'
SECURITY_PASSWORD_HASH = 'plaintext'
SECURITY_PASSWORD_SALT = 'password_salt'
SECURITY_REMEMBER_SALT = 'remember_salt'
SECURITY_RESET_SALT = 'reset_salt'
SECURITY_RESET_WITHIN = '5 days'
SECURITY_CONFIRM_WITHIN = '5 days'
SECURITY_SEND_REGISTER_EMAIL = False

