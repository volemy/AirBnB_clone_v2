#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """
    Amenity class that inherits from BaseModel and Base

    Attributes:
    __tablename__(str): The name of the table
    name (sqlalchemy String): The name of the amenity
    place_amenities(sqlalchemy relationship): A relationship
    """
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
    place_amenities = relationship("Place", secondary="place_amenity",
                                   viewonly=False)
