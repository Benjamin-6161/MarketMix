from flask import Blueprint, render_template, redirect, url_for, flash
from app.extensions import db
from app.models import User
from app.forms import RegistrationForm, LoginForm
from flask_login import login_user, logout_user, login_required

auth = Blueprint('auth', __name__)

# Your routes here...
@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            if user.user_type == 'vendor':
                return redirect(url_for('main.new_vendor'))
            return redirect(url_for('main.index'))
        else:
            flash('Invalid email or password')
    return render_template('auth/login.html', title='Login', form=form)

@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        user.user_type = form.user_type.data
        db.session.add(user)
        db.session.commit()
        flash('You have been registered successfully')        
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html', title='Register', form=form)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))