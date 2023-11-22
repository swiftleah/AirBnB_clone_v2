#!/usr/bin/python3
"""Defines the HBNBCommand class for the console."""

import cmd
from datetime import datetime
import models
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import shlex

CLASSES = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}


class HBNBCommand(cmd.Cmd):
    """Interactive command-line interpreter for HBNB."""
    prompt = '(hbnb) '

    def do_EOF(self, arg):
        """ Handles EOF to exit program """
        return True

    def emptyline(self):
        """ Overrides the emptyline method of CMD """
        return False

    def do_quit(self, arg):
        """ Method to exit the HBNB console"""
        return True

    def _key_value_parser(self, args):
        """Create a dictionary from a list of strings."""
        new_dict = {}
        for arg in args:
            if "=" in arg:
                continue

            pair = arg.split('=', 1)
            key = pair[0]
            value = pair[1]

            if value[0] == value[-1] == '"':
                value = shlex.split(value)[0].replace('_', ' ')
            else:
                try:
                    value = int(value)
                except:
                    try:
                        value = float(value)
                    except:
                        continue
            new_dict[key] = value
        return new_dict

    def do_create(self, arg):
        """Create a new instance of a class."""
        args = arg.split()

        if not args:
            print("** class name missing **")
            return False

        if args[0] in CLASSES:
            class_arguments = args[1:]
            new_dict = self._key_value_parser(class_arguments)
            instance = CLASSES[args[0]](**new_dict)
        else:
            print("** class doesn't exist **")
            return False

        print(instance.id)
        instance.save()

    def do_show(self, arg):
        """Print an instance as a string based on the class and id."""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return False
        if args[0] in CLASSES:
            if len(args) > 1:
                key = args[0] + "." + args[1]
                if key in models.storage.all():
                    print(models.storage.all()[key])
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")
    
    def do_update(self, arg):
        """Update an instance based on the class name, id, attribute & value."""
        args = shlex.split(arg)

        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in CLASSES:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = class_name + "." + args[1]
        all_instances = models.storage.all()

        if instance_id not in all_instances:
            print("** no instance found **")
            return

        instance = all_instances[instance_id]

        if len(args) < 3:
            print("** attribute name missing **")
            return

        attribute_name = args[2]
        if len(args) < 4:
            print("** value missing **")
            return

        value = args[3]
        if attribute_name == "Place":
            if attribute_name in ["number_rooms", "number_bathrooms", "max_guest", "price_by_night"]:
                try:
                    value = int(value)
                except ValueError:
                    value = 0
            elif attribute_name in ["latitude", "longitude"]:
                try:
                    value = float(value)
                except ValueError:
                    value = 0.0

        setattr(instance, attribute_name, value)
        instance.save()

    def do_destroy(self, arg):
        """Delete an instance based on specifications """
        args = shlex.split(arg)
        
        if not args:
            print("** class name missing **")
        elif args[0] not in CLASSES:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            instance_key = args[0] + "." + args[1]
            all_instances = models.storage.all()

            if instance_key not in all_instances:
                print("** no instance found **")
            else:
                all_instances.pop(instance_key)
                models.storage.save()

    def do_all(self, arg):
        """Print string rep of instances."""
        args = shlex.split(arg)
        obj_list = []

        if len(args) == 0:
            obj_dict = models.storage.all()
        elif args[0] in CLASSES:
            obj_dict = models.storage.all(CLASSES[args[0]])
        else:
            print("** class doesn't exist **")
            return False

        obj_list = [str(obj_dict[key]) for key in obj_dict]
        print("[" + ", ".join(obj_list) + "]")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
