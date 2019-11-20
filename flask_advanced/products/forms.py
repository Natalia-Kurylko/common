from wtforms import Form, StringField, TextAreaField, FileField, validators, IntegerField


class AddProductForm(Form):
    name = StringField('name', validators=[validators.Length(min=5, max=30)])
    description = TextAreaField('description', validators=[validators.Length(min=5, max=100)])
    image = FileField('image',validators=[validators.input_required()])
    price = IntegerField('price', validators= [validators.DataRequired()])



