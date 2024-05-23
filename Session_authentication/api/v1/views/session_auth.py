#!/usr/bin/env python3
"""
Session authentication routes
"""
from flask import Blueprint, jsonify, request, abort
from models.user import User
from os import getenv


session_auth = Blueprint('session_auth', __name__)

@session_auth.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login():
    """
    POST /api/v1/auth_session/login
    """
    from api.v1.app import auth

    email = request.form.get('email')
    password = request.form.get('password')

    if email is None or email == '':
        return jsonify({"error": "email missing"}), 400

    if password is None or password == '':
        return jsonify({"error": "password missing"}), 400

    user = User.search({"email": email})
    if len(user) == 0:
        return jsonify({"error": "no user found for this email"}), 404

    user = user[0]
    if not user.is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401

    session_id = auth.create_session(user.id)
    user_json = user.to_json()

    response = jsonify(user_json)
    session_name = getenv("SESSION_NAME")
    response.set_cookie(session_name, session_id)

    return response
