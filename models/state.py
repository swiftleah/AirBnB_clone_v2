#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.engine.file_storage import FileStorage


class State(BaseModel, Base):
    """ State class that inherits from Base """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    if FileStorage == 'db':
        cities = relationship("City", backref="state", cascase="all, delete")
    else:
        @property
        def cities(self):
            """ getter for 'cities' property of 'State' class """
            cityList = []
            for city in models.storage.all("City").values():
                if city.state.id == self.id:
                    cityList.append(city)
            return cityList
