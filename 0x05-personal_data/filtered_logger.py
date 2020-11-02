#!/usr/bin/env python3
"""
Regex-ing
"""
from typing import List
import re


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """returns the log message obfuscated"""
    substitute_msg = message
    for field in fields:
        substitute_msg = re.sub(
            f'(?<={field}=)[^{separator}]*', redaction, substitute_msg)
    return substitute_msg
