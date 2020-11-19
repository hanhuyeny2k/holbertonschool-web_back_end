#!/usr/bin/env python3
"""Authorization Class"""
from flask import request
from typing import List, TypeVar
from os import getenv
from db import DB
from user import User
import uuid
import bcrypt
from sqlalchemy.orm.exc import NoResultFound


def _hash_password(password: str) -> str:
    """the returned string is a salted hash of the input password"""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


class Auth:
    """manage API authentication"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """define which routes don't need authentication"""
        if path is None or not excluded_paths:
            return True
        for i in excluded_paths:
            if i.endswith('*') and path.startswith(i[:-1]):
                return False
            elif i in {path, path + '/'}:
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """request validation"""
        if request is None:
            return None
        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """return None"""
        return None

    def session_cookie(self, request=None):
        """return a cookie value from a request"""
        if request is None:
            return None
        else:
            return request.cookies.get(getenv('SESSION_NAME'))
