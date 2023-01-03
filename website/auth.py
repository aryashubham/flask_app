from flask import Blueprint, render_template, request, flash, url_for, redirect
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password,password):
                return redirect(url_for('views.home'))
            else:
                flash('password is not correct', category="error")
        else:
            flash("user is not exists", category="error")
    return render_template('login.html', user= current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        if len(email) < 4:
            flash("email should be more then 4 characters", category="error")
        elif password1 != password2:
            flash("Password don't match", category="error")
        elif len(password1) < 7:
            flash("password should be more then 7 characters", category="error")
        else:
            user = User(email=email, first_name=firstName, password=generate_password_hash(password1, method='sha256'))
            db.session.add(user)
            db.session.commit()
            flash("Account Created Successfully", category="success")
            return redirect(url_for('views.home'))

    return render_template('signup.html')