#!/usr/bin/env python3
"""
SessionExpAuth class to manage API authentication
"""
import SessionAuth from auth


class SessionExpAuth:
    """Expiration Session"""

    def __init__(self):
        """initialization"""
        try:
            self.session_duration = int(getenv('SESSION_DURATION'))
        except Exception:
            self.session_duration = 0

    def create_session(self, user_id=None):
        """create session"""
        session_ID = super().create_session(user_id)
        if session_ID:
            SessionAuth.user_id_by_session_id[session_ID] = {
                    'user_id': user_id, 'created_at': datetime.now()}
            return session_ID

    def user_id_for_session_id(self, session_id=None):
        """return user_id from session_id"""
        if not session_id:
            return None
        session_dict = SessionExpAuth.user_id_by_session_id.get(session_id)
        if not session_dict:
            return None
        if self.session_duration <= 0:
            return session_dict['user_id']
        if 'created_at' not in session_dict:
            return None
        delta = timedelta(seconds=self.session_duration)
        if session_dict['created_at'] + delta < datetime.now():
            return None
        return session_dict['user_id']
