from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, FileField
from wtforms.fields.simple import SubmitField
from wtforms.validators import URL, DataRequired

class URLForm(FlaskForm):
    url = StringField('URL', validators=[DataRequired(), URL()])
    checkbox = BooleanField("Use custom introspection data from file")
    file = FileField('File')
    
    submit = SubmitField('Connect')
