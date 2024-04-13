from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms.fields import StringField, IntegerField, SubmitField
from wtforms.validators import InputRequired


class AddProductForm(FlaskForm):
    name = StringField("პროდუქტის სახელი", validators=[InputRequired()])
    price = IntegerField("ფასი", validators=[InputRequired()])
    img = FileField("სურათის სახელი", validators=[FileRequired(), FileAllowed(["jpg", "jpeg", "png", "svg"])])
    submit = SubmitField("დამატება")