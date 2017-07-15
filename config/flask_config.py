from os import path, pardir

# Secret Values
CSRF_SESSION_KEY = 'F@4EKKbQu2YewG4hMg7V{)+M'
SECRET_KEY = 'u/C3csJmApsa[9X4EjkU}9]V'

# Flask configurations
HOST = '0.0.0.0'
PORT = 5000
DEBUG = True

# Meta
META_TITLE = 'Your favourite todo list'
META_DESCRIPTION = 'A todo list that allows you to manage all your tasks. Never forget important things again ;)'

# SCSS Options
SCSS_CONFIG_FILE = 'config/scss.json'

# Base directory
BASEDIR = path.abspath(path.join(path.dirname(__file__), pardir))

# Cross-site request forgery configurations
CSRF_ENABLED = True
WTF_CSRF_ENABLED = True

# MongoDB configurations
DB_NAME = 'data.db'
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + path.join(BASEDIR, DB_NAME)
SQLALCHEMY_MIGRATE_REPO = path.join(BASEDIR, 'db_repository')

# Logging configurations
LOG_FILE_MAX_SIZE = '256'
APP_LOG_NAME = 'app.log'
WERKZEUG_LOG_NAME = 'werkzeug.log'

