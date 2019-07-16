from flask import request, render_template, Blueprint, redirect, jsonify, make_response
from sqlalchemy import or_
from short.databases import session

from short.forms import ShortyForm
from short.models import URLS
from .utils import encode

api = Blueprint('', __name__)


@api.route('/', methods=['GET', 'POST'])
def main():
    form = ShortyForm(request.form)
    if request.method == 'POST':
        if form.validate():
            original_url = request.form['url']
            short_url = request.form.get('name')
            if not short_url:
                converted = sum([ord(_) for _ in original_url])
                short_url = encode(converted)
        else:
            return render_template('main.html', form=form, msg='다시 입력해주세요')
        new_urls = URLS(original_url=original_url, short_url=short_url)
        session.add(new_urls)
        session.commit()

        return render_template('main.html', form=form, msg=short_url)

    urls = session.query(URLS).all()
    return render_template('main.html', form=form, urls=urls)


@api.route('/urls', methods=['GET'])
def get_urls():
    urls = session.query(URLS).all()
    if not urls:
        return jsonify(urls=[])
    return jsonify(urls=[dict(original_url=row.original_url,
                              short_url=row.short_url)
                         for row in urls])


@api.route('/urls', methods=['POST'])
def create_short_url():
    data = request.get_json(silent=True)
    if not data.get('url'):
        return make_response(jsonify(msg='url is missing'), 422)

    original_url = data['url']
    short_url = data.get('name')
    if not short_url:
        converted = sum([ord(_) for _ in original_url])
        short_url = encode(converted)

    url_exists = session.query(URLS) \
        .filter(or_(URLS.original_url == original_url,
                    URLS.short_url == short_url)) \
        .first()

    if url_exists:
        return make_response(jsonify(msg=f'{original_url} or {short_url} exists'), 422)

    new_urls = URLS(original_url=original_url, short_url=short_url)
    session.add(new_urls)
    session.commit()
    return jsonify(original_url=original_url, short_url=short_url)


@api.route('/<string:short_url>', methods=['GET'])
def url_converter(short_url):
    url = session.query(URLS).filter_by(short_url=short_url).first()
    if not url:
        return make_response(jsonify(msg='url is missing'), 404)
    return redirect(url.original_url)

