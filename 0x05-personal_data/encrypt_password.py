#!/usr/bin/env python3
"""Check valid password"""
import bcrypt


def hash_password(password: str) -> bytes:
    """Return a salted, hashed password"""
    return bcrypt.hashpw(bytes(password, 'utf-8'), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """Validate the provided password matches the hashed password"""
    return bcrypt.checkpw(bytes(password, 'utf-8'), hashed_password)
