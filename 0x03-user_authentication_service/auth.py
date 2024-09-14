#!/usr/bin/env python3
""" Auth file """
import bcrypt


def _hash_password(password: str) -> bytes:
        """ Hash password """
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)

        return hashed_password
