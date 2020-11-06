#!/usr/bin/env python3
"""Authorization Class"""
from flask import request
from typing import List, TypeVar


class Auth:
    """manage API authentication"""
    
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """define which routes don't need authentication"""
        if path is None:
            return True
        if excluded_paths is None:
            return True
        for i in excluded_paths:
            if i.endswith('*') and path.startswith(i[:-1]):
                return False
            elif i in {path, path + '/'}:
                return False
        return True
    
    def authorization_header(self, request=None) -> str:
        """return None"""
        return None
    
    def current_user(self, request=None) -> TypeVar('User'):
        """return None"""
        return None
