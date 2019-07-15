from flask import Flask, jsonify
from werkzeug.contrib.fixers import ProxyFix

from short.api import api
from short.databases import db


def create_app(config_override=None):
    app = Flask(__name__, template_folder='templates')
    app.wsgi_app = ProxyFix(app.wsgi_app)
    app.config.from_object('config')
    if config_override:
        app.config.update(config_override)
    app.register_blueprint(db)
    app.register_blueprint(api)

    @app.route('/ping')
    def health_check():
        return jsonify(dict(ok='ok'))

    # @app.errorhandler(404)
    # def ignore_error(err):
    #     return jsonify()

    return app

