from flask import request, redirect, render_template, Blueprint
from short.forms import ShortyForm
from .utils import encode

api = Blueprint('', __name__)


@api.route('/', methods=['GET', 'POST'])
def main():
    form = ShortyForm(request.form)
    if request.method == 'POST' and form.validate():
        url = request.form['url']
        name = request.form.get('name')
        converted = sum([ord(_) for _ in url])
        if not name:
            shortened = encode(converted)
        return redirect('/')
    return render_template('main.html', form=form)
