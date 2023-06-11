from apps import app
from flask import render_template, redirect, flash
from apps.forms import LoginForm



@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html", title='Home page')

@app.route('/login', methods=["GET","POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f"Login requested for user{form.username.data}, remember_me{form.remember_me.data}")
        return redirect('/index')
    return render_template('login.html', title="Sign In", form=form)
