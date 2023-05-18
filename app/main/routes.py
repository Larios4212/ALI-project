from flask import render_template, url_for, flash, redirect, request
from .forms import LoginForm, RegistrationForm
from .models import User, Document, AnalysisResult, RecommendedResource
from flask_login import login_user, current_user, logout_user, login_required
from . import main

@main.route("/")
@main.route("/home")
def home():
    return render_template('home.html', title='Home')

@main.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        # TODO: Add user registration logic here
        pass
    return render_template('register.html', title='Register', form=form)

@main.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = LoginForm()
    if form.validate_on_submit():
        # TODO: Add user login logic here
        pass
    return render_template('login.html', title='Login', form=form)
