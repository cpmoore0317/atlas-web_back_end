#!/usr/bin/env python3
"""
auth.py

This module provides the Auth class to manage API authentication.
"""
from flask import request
from typing import List, TypeVar
import os  # Import os to access environment variables


class Auth:
    """
    Auth class to manage the API authentication.

    Methods:
        require_auth(path: str, excluded_paths: List[str]) -> bool
        authorization_header(request=None) -> str
        current_user(request=None) -> TypeVar('User')
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Determines if authentication is required for a given path.

        Args:
        path (str): The path to check.
        excluded_paths (List[str]): A list of paths that do not
        require authentication.

        Returns:
        bool: False for now.
        """
        if path is None:
            return True

        if excluded_paths is None or len(excluded_paths) == 0:
            return True

        # Ensure the path ends with a slash
        if not path.endswith('/'):
            path += '/'

        for excluded_path in excluded_paths:
            if excluded_path.endswith('/'):
                if path == excluded_path:
                    return False
            else:
                if path.rstrip('/') == excluded_path.rstrip('/'):
                    return False

        return True

    def authorization_header(self, request=None) -> str:
        """
        Retrieves the Authorization header from the request.

        Args:
        request (flask.Request): The Flask request object.

        Returns:
        str: None for now.
        """
        if request is None:
            return None

        return request.headers.get('Authorization', None)

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Retrieves the current user from the request.

        Args:
        request (flask.Request): The flask request object.

        Returns:
        TypeVar('User'): None for now.
        """
        return None

    def session_cookie(self, request=None):
        """
        Returns a cookie value from a request.

        Args:
            request (flask.Request): The Flask request object.

        Returns:
            str: The value of the cookie named _my_session_id from the request,
            or None if the request is None or the cookie is not found.
        """
        if request is None:
            return None

        cookie_name = os.getenv('SESSION_NAME')
        if cookie_name is None:
            return None

        return request.cookies.get(cookie_name)
