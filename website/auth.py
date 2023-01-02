from flask import Blueprint, render_template, request, flash


auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html', args= "Test")

@auth.route('/logout')
def logout():
    return '<h2>Logout</h2>'

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
            flash("Account Created Successfully", category="success")

    return render_template('signup.html')