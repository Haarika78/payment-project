from flask import Blueprint, render_template, request, redirect, session

auth_bp = Blueprint('auth', __name__)

USERNAME = "admin"
PASSWORD = "1234"

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form['username']
        pwd = request.form['password']

        if user == USERNAME and pwd == PASSWORD:
            session['user'] = user
            return redirect('/')
        else:
            return "Invalid Credentials"

    return render_template('login.html')


@auth_bp.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('/login')