#!/usr/bin/env python3
"""Test User Model"""

from user import User

print(User.__tablename__)

for column in User.__table__.columns:
    print(f"{column}: {column.type}")
