#!/usr/bin/env python3
"""
SQLAlchemy model DB
"""
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from user import Base, User


class DB:
    """DB class"""

    args_list = ['id', 'email', 'hashed_password', 'session_id', 'reset_token']

    def __init__(self):
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self):
        """session"""
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """Save a user to database"""
        user = User(email=email, hashed_password=hashed_password)
        self._session.add(user)
        self._session.commit()
        return user

    def find_user_by(self, **user_table) -> User:
        """return the first row found in the users table"""
        if not user_table:
            raise InvalidRequestError
        for arg in user_table:
            if arg not in self.args_list:
                raise InvalidRequestError
        user = self._session.query(User).filter_by(**user_table).first()
        if not user:
            raise NoResultFound
        return user

