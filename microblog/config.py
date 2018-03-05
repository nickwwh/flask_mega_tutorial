import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    # Take DB url from enviroment variables or use default value (for developmoent)
    # if no environment variable available, configure a db named app.db in the basedir
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    # Disable Flask-SQLAlchemy feature to signal the app everytime a change is about to be made in the db
    SQLALCHEMY_TRACK_MODIFICATIONS = False