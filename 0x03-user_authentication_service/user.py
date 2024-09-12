#!/usr/bin/env python3
''' user class '''


from sqlalchemy import String, Column, Integer


class User():
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)    
    email = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)
    session_id = Column(String, nullable=True)
    reset_token = Column(String, nullable=True)