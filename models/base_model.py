#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""

from datetime import datetime
from os import getenv
import models
import sqlalchemy
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
import uuid

tf = "%Y-%m-%dT%H:%M:%S.%f"

if models.storage_type == "db":
    Base = declarative_base()
else:
    Base = object


class BaseModel(Base):
    """The BaseModel class from which future classes will be derived"""
    if models.storage_type == "db":
        id = Column(String(60), primary_key=True)
        created_at = Column(DateTime, default=datetime.utcnow)
        updated_at = Column(DateTime, default=datetime.utcnow)

    def __init__(self, *args, **kwargs):
        """Initialization of the base model"""
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
            self.created_at = datetime.strptime(kwargs.get("created_at",
                                             datetime.utcnow()), tf)
            self.updated_at = datetime.strptime(kwargs.get("updated_at",
                                             datetime.utcnow()), tf)
            self.id = kwargs.get("id", str(uuid.uuid4())) or str(uuid.uuid4())
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = self.created_at

    def __str__(self):
        """String representation of the BaseModel class"""
        return "[{:s}] ({:s}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """Updates the attribute 'updated_at' with the current datetime"""
        self.updated_at = datetime.utcnow()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of the instance"""
        new_dict = self.__dict__.copy()
        new_dict["created_at"] = new_dict["created_at"].strftime(tf)
        new_dict["updated_at"] = new_dict["updated_at"].strftime(tf)
        new_dict["__class__"] = self.__class__.__name__

        if "_sa_instance_state" in new_dict:
            del new_dict["_sa_instance_state"]

        return new_dict

    def delete(self):
        """Delete the current instance from the storage"""
        models.storage.delete(self)
