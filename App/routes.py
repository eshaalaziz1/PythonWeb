from flask import render_template, request, redirect, flash, url_for, session
from App.forms import AddTaskForms, LoginForm
from app import app


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