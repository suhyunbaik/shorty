from flask import Flask, Blueprint, jsonify
from werkzeug.contrib.fixers import ProxyFix
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.wsgi_app = ProxyFix(app.wsgi_app)
    app.config['BUNDLE_ERRORS'] = True
    db.init_app(app)

    blueprint = Blueprint('api', __name__, url_prefix='/api')
    app.register_blueprint(blueprint)

    @app.route('/ping')
    def health_check():
        return jsonify(dict(ok='ok'))

    return app

