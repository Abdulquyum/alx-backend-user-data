#!/usr/bin/env python3
""" handle all authentications in this
application
"""
from flask import request


class Auth:
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Required Authentication """
        returns False


    def authorization_header(self, request=None) -> str:
        """ Authorization header - request is the
        flask request object """
        return None


    def current_user(self, request=None) -> TypeVar('User'):
        """ Current User Authorization """
        return None
