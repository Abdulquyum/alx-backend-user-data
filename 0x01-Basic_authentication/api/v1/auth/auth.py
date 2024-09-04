#!/usr/bin/env python3
"""
handle all authentications in this
application
"""
from flask import request


class Auth():
    """" CLASS AUTH """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Check if a path requires authentication.

        Args:
            path (str): The path to check.
            excluded_paths (List[str]): List of paths that do not require authentication.

        Returns:
            bool: True if the path requires authentication, False otherwise.
        """
        return False


    def authorization_header(self, request=None) -> str:
        """Retrieve the Authorization header from the request.

        Args:
            request: The flask request object.

        Returns:
            str: The Authorization header if it exists, None otherwise.
        """
        return None


    def current_user(self, request=None) -> TypeVar('User'):
        """Retrieve the current user (to be implemented).

        Args:
            request: The flask request object.

        Returns:
            User: The currently authenticated user.
        """ 
        return None
