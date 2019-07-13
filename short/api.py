from flask import request, render_template, Blueprint
from flask_sqlalchemy import SQLAlchemy

from short.forms import ShortyForm
from short.models import URLS
from .utils import encode

api = Blueprint('', __name__)
db = SQLAlchemy()


@api.route('/', methods=['GET', 'POST'])
def main():
    form = ShortyForm(request.form)
    if request.method == 'POST' and form.validate():
        original_url = request.form['url']
        short_url = request.form.get('name')
        if not short_url:
            converted = sum([ord(_) for _ in original_url])
            short_url = encode(converted)

        new_urls = URLS(original_url=original_url, short_url=short_url)
        db.session.add(new_urls)
        db.session.commit()
        return render_template('main.html', form=form, msg=short_url)

    return render_template('main.html', form=form)
