#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    #For DBStorage
    cities = relationship("City", backref="state", cascade="all, delete-orphan")

    #For FileStorage
    @property
    def cities(self):
        """Returns the list of City instances with state_id"""
        from models import storage
        new_list = []
        for city in storage.all(City).values():
            if city.state_id == self.id:
                new_list.append(city)
        return new_list
