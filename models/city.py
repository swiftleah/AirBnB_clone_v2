#!/usr/bin/python
""" City class """

import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship

class City(BaseModel, Base):
    """ City that inherits from BaseModel and Base respectively"""
    if models.switch == "db":
        __tablename__ = 'cities'
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        name = Column(String(128), nullable=False)
        places = relationship("Place", backref="cities")

    else:
        state_id = ""
        name = ""

    def __init__(self, *args, **kwargs):
        """ Initialize """
        super().__init__(*args, **kwargs)
