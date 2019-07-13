from os import environ
from short.app import create_app
from config import config_by_name

environment = environ['SHORTY_ENV']
config = config_by_name[environment]
app = create_app(config)


if __name__ == '__main__':
    app.run()
