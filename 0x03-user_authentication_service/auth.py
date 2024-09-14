#!/usr/bin/env python3
""" Auth file """
import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound


class Auth:
    """ Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def _hash_password(password: str) -> bytes:
        """ Hash password """
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)

        return hashed_password

    def register_user(self, email: str, password: str) -> 'User':
        """ Register new users """
        try:
            user_exist = self._db.find_user_by(email=email)
            if user_exist:
                raise ValueError(f'User {email} already exists')

        except NoResultFound:
            hashed_password = self._hash_password(password)

            new_user = User(email=email, hashed_password=hashed_password)

            self._db.add_user(new_user)

            return new_user
