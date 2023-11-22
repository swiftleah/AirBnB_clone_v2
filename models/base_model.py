#!/usr/bin/python3
"""Defines the BaseModel class."""

from datetime import datetime
import models
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
import uuid

TIME_FORMAT = "%Y-%m-%dT%H:%M:%S.%f"

if models.switch == "db":
    Base = declarative_base()
else:
    Base = object


class BaseModel:
    """Base class for future derived classes."""
    if models.switch == "db":
        id = Column(String(60), primary_key=True)
        created_at = Column(DateTime, default=datetime.utcnow)
        updated_at = Column(DateTime, default=datetime.utcnow)

    def __init__(self, *args, **kwargs):
        """Initialize the base model."""
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
            if kwargs.get("created_at", None) and type(self.created_at) is str:
                self.created_at = datetime.strptime(kwargs["created_at"], TIME_FORMAT)
            else:
                self.created_at = datetime.utcnow()
            if kwargs.get("updated_at", None) and type(self.updated_at) is str:
                self.updated_at = datetime.strptime(kwargs["updated_at"], TIME_FORMAT)
            else:
                self.updated_at = datetime.utcnow()
            if kwargs.get("id", None) is None:
                self.id = str(uuid.uuid4())
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = self.created_at

    def __str__(self):
        """String representation of the BaseModel instance."""
        return "[{:s}] ({:s}) {}".format(self.__class__.__name__, self.id,
                                         self.__dict__)

    def save(self):
        """Update 'updated_at' attribute with the current datetime."""
        self.updated_at = datetime.utcnow()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Return a dictionary containing instance key/values."""
        new_dict = self.__dict__.copy()
        if "created_at" in new_dict:
            new_dict["created_at"] = new_dict["created_at"].strftime(TIME_FORMAT)
        if "updated_at" in new_dict:
            new_dict["updated_at"] = new_dict["updated_at"].strftime(TIME_FORMAT)
        new_dict["__class__"] = self.__class__.__name__
        new_dict.pop("_sa_instance_state", None)
        return new_dict

    def delete(self):
        """Delete the instance from storage."""
        models.storage.delete(self)
