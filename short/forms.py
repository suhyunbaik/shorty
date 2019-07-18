from flask_wtf import FlaskForm
from wtforms import StringField, ValidationError
from wtforms.validators import InputRequired

from short.utils import name_regex, url_regex, parsing_url


class ShortyForm(FlaskForm):
    url = StringField('URL', [InputRequired()])
    name = StringField('name')

    def validate_url(self, field):
        regex = url_regex()
        regex_result = regex.search(field.data)
        parsing_result = parsing_url(field.data)
        if regex_result is None:
            if not parsing_result:
                raise ValidationError("url 주소가 잘못된 형식입니다.")

    def validate_name(self, field):
        if not field.data:
            pass
        regex = name_regex()
        result = regex.search(field.data)
        if result is None:
            return ValidationError("단축 url에 특수문자가 포함되어 있습니다.")


