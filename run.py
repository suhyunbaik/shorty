from os import environ
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
from short.app import create_app
from config import config_by_name

environment = environ['SHORTY_ENV']
config = config_by_name[environment]
app = create_app(config)
db = SQLAlchemy(app)
csrf = CSRFProtect(app)

if __name__ == '__main__':
    app.run()
