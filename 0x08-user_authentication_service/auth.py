#!/usr/bin/env python3
"""Authorization Class"""
from db import DB
from user import User
import bcrypt
from sqlalchemy.orm.exc import NoResultFound


def _hash_password(password: str) -> str:
    """the returned string is a salted hash of the input password"""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


class Auth:
    """Auth class to interact with the authentication database"""

    def __init__(self):
        """initialization"""
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """register user using email and password"""
        try:
            if self._db.find_user_by(email=email):
                raise ValueError('User {} already exists'.format(email))
        except NoResultFound:
            return self._db.add_user(email, _hash_password(password))

    def valid_login(self, email: str, password: str) -> bool:
        """Validate credentials"""
        try:
            user = self._db.find_user_by(email=email)
            return bcrypt.checkpw(password.encode('utf-8'),
                                  user.hashed_password)
        except Exception:
            return False
