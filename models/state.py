#!/usr/bin/python3
""" Defines the State class."""
import models
from models.base_model import BaseModel, Base
from models.city import City
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship

class State(BaseModel, Base):
    """Representation of State"""
    if models.storage_type == "db":
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state")
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """Initializes State"""
        super().__init__(*args, **kwargs)

    if models.storage_type != "db":
        @property
        def cities(self):
            """Getter for a list of City instances related to the state"""
            return [city for city in models.storage.all(City).values() if city.state_id == self.id]
