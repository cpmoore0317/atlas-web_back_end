#!/usr/bin/env python3
""" Flask module """
from flask import Flask, jsonify, request
from auth import Auth
import bcrypt

AUTH = Auth()
app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    """Home route that returns JSON"""
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'])
def register():
    """Endpoint for registering a new user."""
    email = request.form.get('email')
    password = request.form.get('password')

    try:
        AUTH.register_user(email, password)
        return jsonify({"email": email, "message": "user created"}), 200
    except ValueError:
        return jsonify({"message": "email already registered"}), 400
    

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
