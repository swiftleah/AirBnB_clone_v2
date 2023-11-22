#!/usr/bin/python3
"""Module that defines DBStorage class."""

import models
from models.amenity import Amenity
from models.base_model import BaseModel, Base
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

classes = {"Amenity": Amenity, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}


class DBStorage:
    """class for DBStorage"""
    __engine = None
    __session = None

    def __init__(self):
        """Instantiates DBStorage object"""
        self.__engine = create_engine(
                f"mysql+mysqldb://{getenv('HBNB_MYSQL_USER')}:{getenv('HBNB_MYSQL_PWD')}@{getenv('HBNB_MYSQL_HOST')}/{getenv('HBNB_MYSQL_DB')}"
                )

        if getenv('HBNB_ENV') == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query on the current database session"""
        new_dict = {}

        for clss in classes:
            if cls is None or cls == classes[clss] or cls == clss:
                objs = self.__session.query(classes[clss]).all()
                for obj in objs:
                    key = f"{obj.__class__.__name__}.{obj.id}"
                    new_dict[key] = obj
        return new_dict

    def new(self, obj):
        """add new object to the current db session"""
        self.__session.add(obj)

    def reload(self):
        """ creates tables based on models if don't exist """
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(sess_factory)

    def save(self):
        """ commits changes of current session """
        self.__session.commit()

    def delete(self, obj=None):
        """ deletes obj from session """
        if obj:
            self.__session.delete(obj)

    def close(self):
        """call remove() method on the private session attribute"""
        self.__session.remove()
