#!/usr/bin/env python
"""Test DB Connection
and new_user"""

from user import User
from db import DB

my_db = DB()

user_1 = my_db.add_user("abd@gmail.com", "123")
print(user_1.id)

user_2 = my_db.add_user("ajb@gmail.com", "345")
print(user_2.id)
