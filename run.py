from os import environ
from config import config_by_name
from short.app import create_app

environment = environ['SHORTY_ENV']
config = config_by_name[environment]
app = create_app(config)


if __name__ == '__main__':
    app.run()
