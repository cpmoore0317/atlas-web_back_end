#!/usr/bin/env python3
"""
Session Auth Module
"""
from api.v1.auth.auth import Auth
import uuid
from typing import TypeVar
from os import getenv


class SessionAuth(Auth):
    """
    SessionAuth class for managing user sessions.

    Attributes:
        user_id_by_session_id (dict): A dictionary to store session IDs and
        their corresponding user IDs.
    """

    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """
        Creates a session ID for a user ID.

        Args:
            user_id (str): The user ID to create a session for.

        Returns:
            str: The session ID if user_id is valid, otherwise None.
        """
        if user_id is None or not isinstance(user_id, str):
            return None

        session_id = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """
        Returns a User ID based on a Session ID.

        Args:
            session_id (str): The session ID to retrieve the user ID for.

        Returns:
            str: The user ID if session_id is valid and exists, otherwise None.
        """
        if session_id is None or not isinstance(session_id, str):
            return None

        return self.user_id_by_session_id.get(session_id)

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
            request (flask.request): The request object to retreive the cookie form.

        Returns:
            str: The cookie value if found, otherwise None.
        """
        if request is None:
            return None

        cookie_name = getenv("SESSION_NAME")
        return request.cookies.get(cookie_name)
