from flask import Flask, jsonify
from flask_wtf import CSRFProtect
from werkzeug.middleware.proxy_fix import ProxyFix
from config import config_by_name
from short.api import api
from short.databases import db

csrf = CSRFProtect()


def create_app(config_name=None):
    app = Flask(__name__, template_folder='templates')
    app.wsgi_app = ProxyFix(app.wsgi_app)
    if not config_name:
        config_name = config_by_name['test']
    app.config.from_object(config_name)
    app.env = config_name

    csrf.exempt(api)
    app.register_blueprint(api)
    app.register_blueprint(db)
    csrf.init_app(app)

    @app.route('/ping')
    def health_check():
        return jsonify(dict(ok='ok'))

    @app.errorhandler(404)
    def ignore_error(err):
        return jsonify()

    return app

