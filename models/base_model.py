#!/usr/bin/python3
"""Defines the BaseModel class."""

from datetime import datetime
import uuid
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
import models

time_format = "%Y-%m-%dT%H:%M:%S.%f"

if models.switch == "db":
    Base = declarative_base()
else:
    Base = object


class BaseModel(Base):
    """The BaseModel class from which future classes will be derived."""
    if models.switch == "db":
        id = Column(String(60), primary_key=True)
        created_at = Column(DateTime, default=datetime.utcnow)
        updated_at = Column(DateTime, default=datetime.utcnow)

    def __init__(self, *args, **kwargs):
        """Initialization of the base model."""
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)

            self.created_at = self.parse_datetime(kwargs.get("created_at", None))
            self.updated_at = self.parse_datetime(kwargs.get("updated_at", None))

            if not kwargs.get("id", None):
                self.id = str(uuid.uuid4())
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = self.created_at

    def parse_datetime(self, dt_str):
        """Parse datetime from string."""
        if dt_str and type(dt_str) is str:
            return datetime.strptime(dt_str, time_format)
        return datetime.utcnow()

    def __str__(self):
        """String representation of the BaseModel class."""
        return "[{:s}] ({:s}) {}".format(self.__class__.__name__, self.id,
                                         self.__dict__)

    def save(self):
        """Update the attribute 'updated_at' with the current datetime."""
        self.updated_at = datetime.utcnow()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Return a dictionary containing all keys/values of the instance."""
        new_dict = self.__dict__.copy()
        new_dict["created_at"] = self.format_datetime(new_dict.get("created_at"))
        new_dict["updated_at"] = self.format_datetime(new_dict.get("updated_at"))
        new_dict["__class__"] = self.__class__.__name__
        new_dict.pop("_sa_instance_state", None)
        return new_dict

    def format_datetime(self, dt):
        """Format datetime to string."""
        if dt:
            return dt.strftime(time_format)
        return None

    def delete(self):
        """Delete the current instance from the storage."""
        models.storage.delete(self)
