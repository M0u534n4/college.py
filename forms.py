from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired
from wtforms.fields import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired


class AddProductForm(FlaskForm):
    name = StringField("პროდუქტის სახელი", validators=[DataRequired()])
    price = IntegerField("ფასი", validators=[DataRequired()])
    img = FileField("სურათის სახელი", validators=[FileRequired()])
    submit = SubmitField("დამატება")