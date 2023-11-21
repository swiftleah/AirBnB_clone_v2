#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models import storage_switch
from sqlalchemy import Column, String
from models.city import City
from sqlalchemy.orm import relationship



class State(BaseModel, Base):
    """ State class that inherits from Base """
    __tablename__ = 'states'
    # name = Column(String(128), nullable=False)
    # if FileStorage == 'db':
    #     cities = relationship("City", backref="state", cascase="all, delete")
    # else:
    #     @property
    #     def cities(self):
    #         """ getter for 'cities' property of 'State' class """
    #         cityList = []
    #         for city in models.storage.all("City").values():
    #             if city.state.id == self.id:
    #                 cityList.append(city)
    #         return cityList
    if storage_switch == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship('City', backref='state',
                              cascade='all, delete, delete-orphan')
    else:
        name = ''

        @property
        def cities(self):
            '''returns the list of City instances with state_id=State.id
                FileStorage relationship between State and City
            '''
            from models import storage
            related_cities = []
            cities_list = storage.all(City)
            for city in cities_list.values():
                if city.state_id == self.id:
                    related_cities.append(city)
            return related_cities