from flask_wtf import FlaskForm
from wtforms import StringField, ValidationError
from wtforms.validators import InputRequired
import re


class ShortyForm(FlaskForm):
    url = StringField('URL', [InputRequired()])
    name = StringField('name')

    def validate_url(self, field):
        regex = re.compile(
            r'^https?://'  # http:// or https://
            r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?|'  # domain
            r'localhost|'  # localhost...
            r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # or ip
            r'(?::\d+)?'  # optional port
            r'(?:/?|[/?]\S+)$', re.IGNORECASE)
        result = regex.search(field.data)
        if result is not None:
            raise ValidationError("url 주소가 잘못되었습니다.")

    def validate_name(self, field):
        if not field.data:
            pass
        if re.match('[a-z]+', field.data):
            return ValidationError("단축 url에 특수문자가 포함되어있습니다.")


