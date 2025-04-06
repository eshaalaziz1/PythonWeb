from wtforms.fields.simple import PasswordField
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Email


class AddTaskForms(FlaskForm):
    task_name = StringField('Enter a text', validators=[DataRequired()])
    submit = SubmitField('Submit')


class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Login")





class StudentForm(FlaskForm):
   idnumber = IntegerField('ID Number', validators=[DataRequired()])
   name = StringField('Name', validators=[DataRequired()])
   grade_level = StringField('Grade Level', validators=[DataRequired()])
   email_address = StringField('Email Address', validators=[DataRequired(), Email()])
   submit = SubmitField('Register Student')


