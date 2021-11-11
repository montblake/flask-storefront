import os


# Determine the folder of the top-level directory of this project
BASEDIR = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    # environment settings
    FLASK_ENV = 'development'
    DEBUG = False
    TESTING = False
    # secret key
    SECRET_KEY = os.getenv('SECRET_KEY', default='development_secret_key')
    # database
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL',
                                        default=f"sqlite:///{os.path.join(BASEDIR, 'instance', 'app.db')}")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    BCRYPT_LOG_ROUNDS = 15
    WTF_CSRF_ENABLED = True


    # Flask-Mail Configuration
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    MAIL_DEFAULT_SENDER = os.environ.get('MAIL_USERNAME')


class ProductionConfig(Config):
    FLASK_ENV = 'production'


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
