"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template,request,redirect,url_for
from Halogen import app

@app.route('/')
@app.route('/home')
@app.route('/login')
def login():
    """Renders the login page."""
    return render_template(
        'login.html',
        title='Halogen Login Page',
    )

@app.route('/handle_login', methods=['GET','POST'])
def handle_login():
    user = (request.form['uname'])
    pw = (request.form['psw'])
    app.logger.info(user)
    if(user == "trainer"):
        return redirect(url_for('home_trainer'))
    else:
        return redirect(url_for('home_student'))

@app.route('/home_student')
def home_student():
    """Renders the home page."""
    return render_template(
        'index_student.html',
        title='Halogen Student Home Page',
        year=datetime.now().year,
    )

@app.route('/home_trainer')
def home_trainer():
    """Renders the home page."""
    return render_template(
        'index_trainer.html',
        title='Halogen Trainer Home Page',
        year=datetime.now().year,
    )

@app.route('/survey')
def survey():
    """Renders the contact page."""
    return render_template(
        'survey.html',
        title='Workshop Survey',
        year=datetime.now().year,
        message='Welcome to survey page!'
    )

@app.route('/insights_trainer')
def insights_trainer():
    """Renders the contact page."""
    return render_template(
        'insights_trainer.html',
        title='Trainer Insights',
        year=datetime.now().year,
        message='Welcome to insights page!'
        )

@app.route('/insights_student')
def insights_student():
    """Renders the contact page."""
    return render_template(
        'insights_student.html',
        title='Student Insights',
        year=datetime.now().year,
        message='Welcome to insights page!'
        )

@app.route('/qa')
def qa():
    """Renders the contact page."""
    return render_template(
        'qa.html',
        title='Questionnaire Analysis',
        year=datetime.now().year,
        message='Welcome to survey page!'
    )
