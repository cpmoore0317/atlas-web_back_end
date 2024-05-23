#!/usr/bin/env python3
"""
Flask app initialization for the API.
"""
from os import getenv
from flask import Flask, jsonify, abort, request
from api.v1.views import app_views
from flask_cors import CORS
from api.v1.auth.auth import Auth
from api.v1.auth.session_auth import SessionAuth


app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})

auth = None
auth_type = getenv("AUTH_TYPE", "basic")

if auth_type == "session_auth":
    from api.v1.auth.session_auth import SessionAuth
    auth = SessionAuth()
else:
    from api.v1.auth.auth import Auth
    auth = Auth()


@app.before_request
def before_request():
    """
    Before request handler to check for authentication.
    """
    excluded_paths = ['/api/v1/status/', '/api/v1/unauthorized/', '/api/v1/forbidden/', '/api/v1/auth_session/login/']

    if auth and auth.require_auth(request.path, excluded_paths):
        if not auth.authorization_header(request) and not auth.session_cookie(request):
            abort(401)
        if auth.current_user(request) is None:
            abort(403)


@app.errorhandler(401)
def unauthorized(error):
    """
    Unauthorized error handler.
    """
    return jsonify({"error": "Unauthorized"}), 401


@app.errorhandler(403)
def forbidden(error):
    """
    Forbidden error handler.
    """
    return jsonify({"error": "Forbidden"}), 403


@app.errorhandler(404)
def not_found(error):
    """
    Not found error handler.
    """
    return jsonify({"error": "Not found"}), 404

if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=int(port))
