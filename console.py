#!/usr/bin/python3
"""
This will be the command line interpreter module
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
        print()
        return True

    def emptyline(self):
        """
        Empty line behavior - doesn't execute anything.
        """
        pass

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id.
        Ex: $ create BaseModel
        If the class name is missing, print ** class name missing ** (ex: $ create)
        If the class name doesn’t exist, print ** class doesn't exist ** (ex: $ create MyModel)
        """
        if not arg:
            print("** class name missing **")
            return

        classes = {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "Amenity": Amenity,
            "City": City,
            "Place": Place,
            "Review": Review
        }

        class_name = arg.split()[0]
        if class_name not in classes:
            print("** class doesn't exist **")
            return

        instance = classes[class_name]()
        instance.save()
        print(instance.id)

    def do_show(self, arg):
        """
        Prints the string representation of an instance based on the class name and id.
        Ex: $ show BaseModel 1234-1234-1234.
        If the class name is missing, print ** class name missing ** (ex: $ show)
        If the class name doesn’t exist, print ** class doesn't exist ** (ex: $ show MyModel)
OBOBOB        If the id is missing, print ** instance id missing ** (ex: $ show BaseModel)
        If the instance of the class name doesn’t exist for the id, print ** no instance found ** (ex: $ show BaseModel 121212)
        """
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        class_name = args[0]
OBOBOB        if class_name not in storage.classes():
            print("** class doesn't exist **")
OBOBOB            return

        if len(args) < 2:
OBOBOB            print("** instance id missing **")
OBOBOB            return
OBOBOB
        key = "{}.{}".format(class_name, args[1])
OBOBOB        if key not in storage.all():
            print("** no instance found **")
            return

        print(storage.all()[key])

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id (save the change into the JSON file).
        Ex: $ destroy BaseModel 1234-1234-1234.
        If the class name is missing, print ** class name missing ** (ex: $ destroy)
        If the class name doesn’t exist, print ** class doesn't exist ** (ex:$ destroy MyModel)
        If the id is missing, print ** instance id missing ** (ex: $ destroy BaseModel)
        If the instance of the class name doesn’t exist for the id, print ** no instance found ** (ex: $ destroy BaseModel 121212)
        """
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        class_name = args[0]
        if class_name not in storage.classes():
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        key = "{}.{}".format(class_name, args[1])
        if key not in storage.all():
            print("** no instance found **")
            return

        del storage.all()[key]
        storage.save()

    def do_all(self, arg):
        """
        Prints all string representation of all instances based or not on the class name.
        Ex: $ all BaseModel or $ all.
        The printed result must be a list of strings (like the example below)
        If the class name doesn’t exist, print ** class doesn't exist ** (ex: $ all MyModel)
        """
        objs = []
        if arg:
            class_name = arg.split()[0]
            if class_name not in storage.classes():
                print("** class doesn't exist **")
                return
            objs = [str(obj) for obj in storage.all().values() if type(obj).__name__ == class_name]
        else:
            objs = [str(obj) for obj in storage.all().values()]

        print(objs)

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file).
        Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com".
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        Only one attribute can be updated at the time
        You can assume the attribute name is valid (exists for this model)
        The attribute value must be casted to the attribute type
        If the class name is missing, print ** class name missing ** (ex: $ update)
        If the class name doesn’t exist, print ** class doesn't exist ** (ex: $ update MyModel)
        If the id is missing, print ** instance id missing ** (ex: $ update BaseModel)
        If the instance of the class name doesn’t exist for the id, print ** no instance found ** (ex: $ update BaseModel 121212)
        If the attribute name is missing, print ** attribute name missing ** (ex: $ update BaseModel existing-id)
        If the value for the attribute name doesn’t exist, print ** value missing ** (ex: $ update BaseModel existing-id first_name)
        All other arguments should not be used (Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com" first_name "Betty" = $ update BaseModel 1234-1234-1234 email "aibnb@mail.com")
        id, created_at and updated_at cant’ be updated. You can assume they won’t be passed in the update command
        Only “simple” arguments can be updated: string, integer and float. You can assume nobody will try to update list of ids or datetime
        """
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        class_name = args[0]
        if class_name not in storage.classes():
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        key = "{}.{}".format(class_name, args[1])
        if key not in storage.all():
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return

        if len(args) < 4:
            print("** value missing **")
            return

        instance = storage.all()[key]
        attr_name = args[2]
        attr_value = args[3]

        if hasattr(instance, attr_name):
            attr_value = type(getattr(instance, attr_name))(attr_value)
            setattr(instance, attr_name, attr_value)
            storage.save()
        else:
            print("** attribute doesn't exist **")

    def default(self, line):
        """
        Default behavior for commands.
        """
        if line == "quit":
            return self.do_quit(line)
        elif line == "EOF":
            return self.do_EOF(line)
        else:
            print("*** Unknown syntax: {}".format(line))


if __name__ == '__main__':
    HBNBCommand().cmdloop()

