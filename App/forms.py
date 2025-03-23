from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.fields.simple import PasswordField
from wtforms.validators import DataRequired

class AddTaskForms(FlaskForm):
    task_name = StringField('Enter a text', validators=[DataRequired()])
    submit = SubmitField('Submit')


class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Login")
