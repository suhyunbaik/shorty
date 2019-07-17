import re

from flask import request, render_template, Blueprint, redirect, jsonify, make_response
from short.databases import session

from short.forms import ShortyForm
from short.models import URLS
from .utils import encode

api = Blueprint('', __name__)


def create_short_url(original_url):
    converted = sum([ord(_) for _ in original_url])
    return encode(converted)


@api.route('/', methods=['GET', 'POST'])
def main():
    form = ShortyForm(request.form)
    if request.method == 'POST':
        if not form.validate():
            return render_template('main.html', form=form, msg='다시 입력해주세요')

        original_url = request.form['url']
        short_url = request.form.get('name')
        if not short_url:
            short_url = create_short_url(original_url)

        new_urls = URLS(original_url=original_url, short_url=short_url)
        session.add(new_urls)
        session.commit()
        urls = session.query(URLS).all()
        return render_template('main.html', form=form, msg=short_url, urls=urls)

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
def get_short_url():
    data = request.get_json(silent=True)
    result = validate_url_and_name(data)
    if result:
        return make_response(jsonify(msg=result), 422)

    original_url = data['url']
    short_url = data.get('name')

    if not short_url:
        short_url = create_short_url(original_url)

    url_exists = session.query(URLS) \
        .filter(URLS.short_url == short_url) \
        .first()

    if url_exists:
        return make_response(jsonify(msg=f'{short_url} exists'), 422)

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


def validate_url_and_name(data):
    regex = re.compile(
        r'^https?://'  # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?|'  # domain
        r'localhost|'  # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # or ip
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    result = regex.search(data['url'])
    if result is not None:
        return 'url 주소가 잘못되었습니다.'

    if data.get('name'):
        regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
        if regex.search(data['name']):
            return '단축 url에 특수문자가 포함되어있습니다.'

