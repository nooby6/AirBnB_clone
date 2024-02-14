#!/usr/bin/python3
"""
Module for the command line interpreter.
"""

import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models import storage
import re

class HBNBCommand(cmd.Cmd):
    """
    Command line interpreter class.
    """
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """
        Quit command to exit the program.
        """
        return True

    def do_EOF(self, arg):
        """
        Cleanly exits the program on receiving end-of-file marker (Ctrl+D).
        """
        return True

    def emptyline(self):
        """
        Empty line behavior - doesn't execute anything.
        """
        pass

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel, saves it to the JSON file, and prints the id.
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in ['BaseModel', 'User', 'State', 'Amenity', 'City', 'Place', 'Review']:
            print("** class doesn't exist **")
            return
        new_instance = eval(class_name)()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """
        Prints the string representation of an instance based on the class name and id.
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        class_name = args[0]
        instance_id = args[1]
        if class_name not in ['BaseModel', 'User', 'State', 'Amenity', 'City', 'Place', 'Review']:
            print("** class doesn't exist **")
            return
        key = "{}.{}".format(class_name, instance_id)
        instance = storage.get_instance(key)
        if instance is None:
            print("** no instance found **")
        else:
            print(instance)

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id (save the change into the JSON file).
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        class_name = args[0]
        instance_id = args[1]
        if class_name not in ['BaseModel', 'User', 'State', 'Amenity', 'City', 'Place', 'Review']:
            print("** class doesn't exist **")
            return
        key = "{}.{}".format(class_name, instance_id)
        if key not in storage.all():
            print("** no instance found **")
            return
        del storage.all()[key]
        storage.save()

    def do_all(self, arg):
        """
        Prints all string representations of all instances based or not on the class name.
        """
        args = arg.split()
        if not args:
            print([str(instance) for instance in storage.all().values()])
            return
        class_name = args[0]
        if class_name not in ['BaseModel', 'User', 'State', 'Amenity', 'City', 'Place', 'Review']:
            print("** class doesn't exist **")
            return
        print([str(instance) for key, instance in storage.all().items() if key.split('.')[0] == class_name])

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id by adding or updating attribute.
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        class_name = args[0]
        instance_id = args[1]
        if class_name not in ['BaseModel', 'User', 'State', 'Amenity', 'City', 'Place', 'Review']:
            print("** class doesn't exist **")
            return
        key = "{}.{}".format(class_name, instance_id)
        if key not in storage.all():
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        attribute_name = args[2]
        attribute_value = args[3]
        instance = storage.get_instance(key)
        setattr(instance, attribute_name, attribute_value)
        storage.save()

    def do_count(self, arg):
        """
        Count instances of a class.
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in ['BaseModel', 'User', 'State', 'Amenity', 'City', 'Place', 'Review']:
            print("** class doesn't exist **")
            return
        print(len([instance for key, instance in storage.all().items() if key.split('.')[0] == class_name]))

    def do_help(self, arg):
        """
        List available commands with "help" or detailed help with "help cmd".
        """
        cmd.Cmd.do_help(self, arg)

if __name__ == "__main__":
    HBNBCommand().cmdloop()
