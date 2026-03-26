import sys
import os

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from flask import Flask
from routes.payment_routes import payment_bp
from routes.auth_routes import auth_bp
from database.db import init_db

# ✅ FIRST create app
app = Flask(__name__)

# ✅ THEN set secret key
app.secret_key = "secret123"

# ✅ THEN register routes
app.register_blueprint(payment_bp)
app.register_blueprint(auth_bp)

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
    _