from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms.fields import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired


class AddProductForm(FlaskForm):
    name = StringField("პროდუქტის სახელი", validators=[DataRequired()])
    price = IntegerField("ფასი", validators=[DataRequired()])
    img = FileField("სურათის სახელი", validators=[FileRequired(), FileAllowed(["jpg", "jpeg", "png", "svg"])])
    submit = SubmitField("დამატება")