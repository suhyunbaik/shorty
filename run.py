from os import environ
from app import create_app

config_name = environ['SHORTY_ENV']
app = create_app(config_name)

if __name__ == '__main__':
    app.run()
