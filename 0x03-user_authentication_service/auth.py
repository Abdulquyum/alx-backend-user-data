#!/usr/bin/env python3
""" Auth file """
import bcrypt
from db import DB
from user import User

class Auth:
    """ Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def _hash_password(self, password: str) -> bytes:
        """ Hash password """
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)

        return hashed_password

    def register_user(self, email: str, password: str) -> 'User':
        """ Register new users """
        if email in User:
            raise ValueError('User {User[email]} already exists')

        user = self._hash_password(password)

        self._db(user)

        return user