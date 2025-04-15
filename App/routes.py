import pandas as pd

from flask import render_template, request, redirect, flash, url_for, session
from flask_wtf import FlaskForm
from werkzeug.routing import ValidationError
from wtforms.fields.simple import StringField

from App.forms import AddTaskForms, LoginForm
from app import app, db
from models import Student
import forms


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/form', methods=['GET', 'POST'])
def form():
    form = AddTaskForms()
    if form.validate_on_submit():
        return render_template('form.html', form=form, text=form.task_name.data)
    return render_template('form.html', form=form)


@app.route('/rectangle', methods=['GET', 'POST'])
def rectangle():
    result = None
    if request.method == 'POST':
        # Get the length and width values from the form
        length = float(request.form['length'])
        width = float(request.form['width'])

        # Calculate area or perimeter based on the button clicked
        if request.form['action'] == 'area':
            result = length * width
        elif request.form['action'] == 'perimeter':
            result = 2 * (length + width)

    return render_template('rectangle.html', result=result)



@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        # Hardcoded authentication check
        if username == "admin" and password == "hello123123":
            session['username'] = username  # Store username in session
            flash("Login successful!", "success")
            return redirect(url_for('login'))  # Stay on the same page to show the username
        else:
            flash("Invalid username or password.", "danger")

    return render_template('login.html', form=form, username=session.get('username'))

@app.route('/logout')
def logout():
    session.pop('username', None)  # Remove username from session
    flash("You have been logged out.", "info")
    return redirect(url_for('login'))




@app.route('/students', methods=['GET', 'POST'])
def students():
   form = forms.StudentForm()
   students = Student.query.all()  # Retrieve all students


   if form.validate_on_submit():
       # Get form data
       idnumber = form.idnumber.data
       name = form.name.data
       grade_level = form.grade_level.data
       email_address = form.email_address.data


       # Check if email already exists
       existing_student = Student.query.filter_by(email_address=email_address).first()
       if existing_student:
           flash("Email already registered!", "danger")
       else:
           new_student = Student(idnumber=idnumber, name=name, grade_level=grade_level, email_address=email_address)
           db.session.add(new_student)
           db.session.commit()
           flash("Student registered successfully!", "success")
           return redirect(url_for('students'))  # Prevent form resubmission


   return render_template('students.html', form=form, students=students)
@app.route('/', methods=['GET', 'POST'])
def register():
    form = forms.StudentForm()
    students = Student.query.all()

    if form.validate_on_submit():
        new_student = Student(
            idnumber=form.idnumber.data,
            name=form.name.data,
            grade_level=form.grade_level.data,
            email_address=form.email_address.data
        )
        db.session.add(new_student)
        db.session.commit()
        return redirect(url_for('register'))  # Refresh the page

    return render_template('register.html', form=form, students=students)

import re
from email.utils import parseaddr
# Custom email validator
def validate_email(form, field):
    email = field.data
    if parseaddr(email)[1] == '':  # If the email is invalid
        raise ValidationError('Invalid email address')

# Use it in the form
class MyForm(FlaskForm):
    email = StringField('Email', validators=[validate_email])



@app.route('/dashboard')
def dashboard():
    df = pd.read_csv('static/schools.csv')

    top_roles = df['Role Modified'].value_counts().nlargest(10)
    conference_counts = df['Conference'].value_counts()
    country_counts = df['Country'].value_counts()

    locations = df.apply(lambda row: {
        "name": f"{row['first_name']} {row['last_name']}",
        "school": row["Your school"],
        "lat": row["Lat"],
        "lng": row["Long"]
    }, axis=1).tolist()

    return render_template("dashboard.html",
                           top_roles=top_roles,
                           conference_counts=conference_counts,
                           country_counts=country_counts,
                           locations=locations)
