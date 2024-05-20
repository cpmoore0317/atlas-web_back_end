#!/usr/bin/env python3
"""
auth.py

This module provides the Auth class to manage API authentication.
"""
from flask import request
from typing import List, TypeVar


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
        return False

    def authorization_header(self, request=None) -> str:
        """
        Retrieves the Authorization header from the request.

        Args:
        request (flask.Request): The Flask request object.

        Returns:
        str: None for now.
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Retrieves the current user from the request.

        Args:
        request (flask.Request): The flask request object.

        Returns:
        TypeVar('User'): None for now.
        """
        return None
