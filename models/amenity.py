#!/usr/bin/python
"""Defines the Amenity class."""

import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

class Amenity(BaseModel, Base):
    """Representation of an Amenity."""
    if models.switch == 'db':
        __tablename__ = 'amenities'
        name = Column(String(128), nullable=False)
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """Initializes an Amenity instance."""
        super().__init__(*args, **kwargs)
