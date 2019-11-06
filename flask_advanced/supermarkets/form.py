from wtforms import Form, StringField, TextAreaField, FileField, validators, IntegerField


class AddSupermarketForm(Form):
    name = StringField('name', validators=[validators.Length(min=5, max=30)])
    location = TextAreaField('location', validators=[validators.Length(min=5, max=30)])
    image = FileField('image',validators=[validators.input_required()])
