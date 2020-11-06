#!/usr/bin/env python3
"""Authorization Class"""
from flask import request
from typing import List, TypeVar

class Auth:
    """manage API authentication"""
    
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """return False"""
        return False
    
    def authorization_header(self, request=None) -> str:
        """return None"""
        return None
    
    def current_user(self, request=None) -> TypeVar('User'):
        """return None"""
        return None
