#!/usr/bin/python3
"""
This will be the command line interpreter module
"""
import cmd
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    this creates an entry point for the command line interpreter
    """
    prompt = "(hbnb)"
    classes = ("BaseModel", "User", "State", "Amenity", "City", "Place", "Review")


    def do_quit(self, line):
        """
        console exit command
        """
        return True # Return True to indicate that the program should exit

    def do_EOF(self, line):
        """
        console exit command
        """
        return True # Return True to indicate that the program should exit

    def do_create(self, name):
        """
        Creates a new instance of the 'Base Model'
        saves the instance to the JSON file
        Prints the id
        """
        if name:
            #check if the class exists
            if class_exists(name):
                new_instance = Base model()
                new_instance.save() #implement save method in BaseModel class
                print(new_instance.id)
            else:
                print("Class '{}' doesn't exist".format(name))
        else:
            print("Usage: create <class_name>")

    def emptyline (self):
        """
        an empty line + ENTER shouldn’t execute anything
        """
        return

    def do_show(self, args):
        """
        Prints the string represemtation of an instance based on class name and id.
        """
        if not args:
            print("** class name missing **")
            return
        class_name, -, instance_id = args.partition(' ')

        if not class_name:
            print("** class name missing **")
            return

        if class_name not in classes:
            print("** class doesn't exist **")
            return

        if not instance_id:
            print("** instance id missing **")
            return

        instance = storage.get(class_name, instance_id)
        if not instance:
            print("** no instance found **")
            return

        print(instance)

    def do_destroy(self, args):
        """
        Deletes an instance based on the class name and ID 
        Save the change into the JSON file.
        """
        if not args:
            print("** class name missing **")
            return

        class_name, _, instance_id = args.partition(' ')

        if not class_name:
            print("** class name missing **")
            return

        if class_name not in classes:
            print("** class doesn't exist **")
            return

        if not instance_id:
            print("** instance id missing **")
            return

        instance = storage.get(class_name, instance_id)
        if not instance:
            print("** no instance found **")
            return

        storage.delete(instance)
        storage.save()

    def do_all(self, args):
        """
        Prints all string representations of all instances based on or not on the class name.
        """
        if args:
            class_name = args.split()[0]

            if class_name not in classes:
                print("** class doesn't exist **")
                return
            instances = storage.all(class_name)
        else:
            instances = storage.all()

        for instance in instances.values():
            print(instance)

    def do_update(self, args):
        """
        Updates an instance based on the class name and id by adding or updating attribute
        (save the change into the JSON file).
        """
        if not args:
            print("** class missing **")
            return
        
        class_name, _, args - args.partition(' ')

        if not class_name:
            print("** class name missing **")
            return

        if class_name not in classes:
            print("** class doesn't exist **")
            return

        instance_id, _, args = args.partition(' ')

        if not instance_id:
            print("** instance id mising **")
            return

        instance = storage.get(class_name, instance_id)
        if not instance:
            print("** no instance found **")
            return

        attr_name, _, attr_value = args.partition(' ')

        if not attr_name:
            print("** attribute name missing **")
            return

        if not attr_value:
            print("** value missing **")
            return

        # Update attribute of the instance

        setattr(instance, attr_name, attr_value)
        
        # save changes to JSON file
        instance.save()

    def do_help(self, args):
        """
        List available commands with "help" or detailed help with "help cmd"
        """
        # Call the  do_help method of the parent class to provide default behaviour
        cmd.Cmd.do_help(self, args)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
