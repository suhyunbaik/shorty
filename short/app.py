from flask import Flask, jsonify, render_template, request, redirect
from flask_wtf import CSRFProtect
from werkzeug.contrib.fixers import ProxyFix
from short.forms import ShortyForm
from short.utils import Base62

csrf = CSRFProtect()


def create_app(config_name):
    app = Flask(__name__)
    app.wsgi_app = ProxyFix(app.wsgi_app)
    app.config.from_object(config_name)
    csrf.init_app(app)

    @app.route('/ping')
    def health_check():
        return jsonify(dict(ok='ok'))

    @app.errorhandler(404)
    def ignore_error(err):
        return jsonify()

    @app.route('/', methods=['GET', 'POST'])
    def main():
        form = ShortyForm(request.form)
        if request.method == 'POST' and form.validate():
            url = request.form['url']
            name = request.form['name']
            # converted = sum([ord(_) for _ in url])
            base62 = Base62()
            return redirect('/')
        return render_template('main.html', form=form)

    return app

