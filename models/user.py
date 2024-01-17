#!/usr/bin/python3
"""This module defines the User class"""
from sqlalchemy import Column, String
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from models.place import place
from sqlalchemy.ext.declarative import declarative_base


class User(BaseModel, Base):
    """ This class representing a user by various attributes"""

    __tablename__ = "users"

    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)

    places = relationship(
        "Place",
        cascade='all, delete, delete-orphan',
        backref="user")
