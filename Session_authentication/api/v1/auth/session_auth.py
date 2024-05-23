#!/usr/bin/env python3
"""
Session Auth Module
"""
from api.v1.auth.auth import Auth
import uuid


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
