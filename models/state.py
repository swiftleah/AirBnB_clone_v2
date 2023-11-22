#!/usr/bin/python3
"""Defines the State class."""

import models
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship

class State(BaseModel, Base):
    """Representation of a state."""
    if models.switch == "db":
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state")
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """Initializes a state instance."""
        super().__init__(*args, **kwargs)

    if models.switch != "db":
        @property
        def cities(self):
            """Getter for a list of city instances related to the state."""
            return [city for city in models.storage.all(City).values()
                    if city.state_id == self.id]
