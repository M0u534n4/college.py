from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms.fields import StringField, IntegerField, SubmitField
from wtforms.validators import InputRequired, DataRequired


class AddProductForm(FlaskForm):
    name = StringField("პროგრამის სახელი", validators=[InputRequired()])
    price = StringField("დონე", validators=[InputRequired()])
    img = FileField("სურათის სახელი", validators=[FileRequired(), FileAllowed(["jpg", "jpeg", "png", "svg"])])
    submit = SubmitField("დამატება")


class AddPostForm(FlaskForm):
    name = StringField("discription", validators=[InputRequired()])
    img = FileField("სურათის სახელი", validators=[FileRequired(), FileAllowed(["jpg", "jpeg", "png", "svg"])])
    submit = SubmitField("დამატება")



class FileUpload(FlaskForm):
    name = StringField("discription", validators=[InputRequired()])
    file = FileField('File', validators=[DataRequired(), FileAllowed(['pdf'], 'Only PDF files allowed!')])
    submit = SubmitField('Upload')