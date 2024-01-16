#!/usr/bin/python3
"""This module defines the User class"""

from sqlalchemy import Column, Integer, String
from models.base_model import BaseModel, Base

class User(BaseModel, Base):
    """Class representing a user with different attributes"""

    __tablename__ = "users"

    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
