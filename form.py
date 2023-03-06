from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, IntegerField, BooleanField, SelectField
from wtforms.validators import DataRequired, Length

class MovieForm(FlaskForm):
    title = StringField('title', validators=[DataRequired(), Length(min=4, max=255)])
    overview =  TextAreaField('overview', validators=[DataRequired(), Length(min=4, max=255)])
    release_date = IntegerField('release_date', validators=[DataRequired(), Length(min=6, max=8)])
    poster_path = TextAreaField('poster_path', validators=[DataRequired(), Length(min=4, max=255)])
    submit = SubmitField("submit")
