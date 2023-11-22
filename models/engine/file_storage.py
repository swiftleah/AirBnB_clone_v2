#!/usr/bin/python3
"""Defines the FileStorage class."""
import json
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


classes = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}


class FileStorage:
    """ Serializes instances -> JSON file -> deserializes -> instances """
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """ Returns dictionary __objects """
        if cls:
            return {key: value for key, value in self.__objects.items() if cls == value.__class__ or cls == value.__class__.__name__}
        return self.__objects

    def new(self, obj):
        """ Sets in __objects the obj with key <obj class name>.id """
        if obj:
            key = f"{obj.__class__.__name__}.{obj.id}"
            self.__objects[key] = obj

    def save(self):
        """ Serializes __objects to JSON file ( __file_path"""
        json_objects = {key: value.to_dict() for key, value in self.__objects.items()}
        with open(self.__file_path, 'w') as f:
             json.dump(json_objects, f)

    def reload(self):
        """ Deserializes JSON file to __objects """
        try:
            with open(self.__file_path, 'r') as file:
                jsn = json.load(file)
            for key in jsn:
                self.__objects[key] = classes[jsn[key]["__class__"]](**jsn[key])
        except:
            pass

    def delete(self, obj=None):
        """delete obj from __objects if it’s inside"""
        if obj is not None:
            key = obj.__class__.__name__ + '.' + obj.id
            if key in self.__objects:
                del self.__objects[key]

    def close(self):
        """call reload() method for deserializing the JSON file to objects"""
        self.reload()
