from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Length

class AddMovieForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(min=2, max=50)])
    duration_minutes = IntegerField('Duration in minutes', validators=[DataRequired()])
    genre = StringField('Genre', validators=[DataRequired(), Length(min=2, max=100)])
    short_description = StringField('Short description', validators=[DataRequired(), Length(min=2, max=200)])
    submit = SubmitField('Add Movie')
