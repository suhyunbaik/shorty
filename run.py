from os import environ
from app import create_app
from config import config_by_name

config = config_by_name[environ['SHORTY_ENV']]
app = create_app(config)

if __name__ == '__main__':
    app.run()
