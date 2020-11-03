#!/usr/bin/env python3
"""
Read and filter data
"""
from typing import List
import re
import logging
import os
import mysql.connector

PII_FIELDS = ("name", "email", "phone", "ssn", "password")


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class"""

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """Format a record"""
        return filter_datum(self.fields, self.REDACTION,
                            super().format(record), self.SEPARATOR)


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """returns the log message obfuscated"""
    substitute_msg = message
    for field in fields:
        substitute_msg = re.sub(
                f'(?<={field}=)[^{separator}]*', redaction, substitute_msg)
    return substitute_msg


def get_logger() -> logging.Logger:
    """Get a logger that redacts sensitive info"""
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False
    handler = logging.StreamHandler()
    handler.setFormatter(RedactingFormatter(PII_FIELDS))
    logger.addHandler(handler)
    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """Get a connection to the database specified in env variables"""
    user = os.getenv('PERSONAL_DATA_DB_USERNAME', 'root')
    passwd = os.getenv('PERSONAL_DATA_DB_PASSWORD', '')
    host = os.getenv('PERSONAL_DATA_DB_HOST', 'localhost')
    name = os.getenv('PERSONAL_DATA_DB_NAME')
    connection = mysql.connector.connect(
        user=user,
        password=passwd,
        host=host,
        database=name)
    return connection


def main():
    """Print out contents of a database"""
    cnx = get_db()
    cursor = cnx.cursor()
    cursor.execute('SELECT * FROM users;')
    fields = PII_FIELDS + ("ip", "last_login", "user_agent")
    logger = get_logger()
    for row in cursor:
        msg = "; ".join(
            f'{fields[i]}={row[i]}' for i in range(len(fields))) + ';'
        logger.log(logging.INFO, msg)
    cursor.close()
    cnx.close()


if __name__ == '__main__':
    main()
