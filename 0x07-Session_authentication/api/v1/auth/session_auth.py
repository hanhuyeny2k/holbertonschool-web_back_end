#!/usr/bin/env python3
"""Session Authorization
"""
from models.user import User
from api.v1.auth.auth import Auth
import uuid


class SessionAuth(Auth):
    """Session Authorization"""
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """creates a Session ID for a user_id"""
        if user_id is None or not isinstance(user_id, str):
            return None
        else:
            session_id = str(uuid.uuid4())
            SessionAuth.user_id_by_session_id[session_id] = user_id
            return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """return a User ID based on Session ID"""
        if session_id is None or not isinstance(session_id, str):
            return None
        else:
            return SessionAuth.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """return a User instance based on a cookie value"""
        return User.get(
            self.user_id_for_session_id(self.session_cookie(request)))

    def destroy_session(self, request=None):
        """deletes the user session / logout"""
        if request is None:
            return False
        session_ID = self.session_cookie(request)
        if request is not session_ID:
            return False
        if request is not self.user_id_for_session_id(session_ID):
            return False
        self.user_id_by_session_id.pop(session_ID)
        return True
