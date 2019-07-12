from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import URL


class ShortyForm(FlaskForm):
    url = StringField('URL', validators=[URL(require_tld=True, message="Invalid URL")])
    name = StringField('name')