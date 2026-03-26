from flask import Blueprint, render_template, redirect
from services.payment_service import create_checkout_session
from database.db import get_db
from flask import session, redirect


payment_bp = Blueprint('payment', __name__)

@payment_bp.route('/')
def home():
    if 'user' not in session:
        return redirect('/login')
    return render_template('index.html')

@payment_bp.route('/checkout', methods=['POST'])
def checkout():
    session = create_checkout_session()
    return redirect(session.url)

@payment_bp.route('/success')
def success():
    return render_template('success.html')

@payment_bp.route('/cancel')
def cancel():
    return render_template('cancel.html')

@payment_bp.route('/history')
def history():
    conn = get_db()
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM transactions")
    data = cursor.fetchall()
    
    conn.close()
    
    return render_template('history.html', transactions=data)

