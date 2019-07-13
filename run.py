from os import environ
from flask_sqlalchemy import SQLAlchemy
from short.app import create_app
from config import config_by_name

environment = environ['SHORTY_ENV']
config = config_by_name[environment]
app = create_app(config)
db = SQLAlchemy(app)

if __name__ == '__main__':
    app.run()
