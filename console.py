#!/usr/bin/python3
<<<<<<< HEAD
"""
This will be the command line interpreter module
"""
=======
"""This module defines a command interpreter"""
>>>>>>> c76cd43f2ca67d0df5b6a1792b3c70adc94e336b
import cmd
from models.base_model import BaseModel
<<<<<<< HEAD
from models.user import User
from models.state import State
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
=======
>>>>>>> c76cd43f2ca67d0df5b6a1792b3c70adc94e336b
from models import storage


class HBNBCommand(cmd.Cmd):
    """_summary_

    Args:
        cmd (_type_): _description_
    """
<<<<<<< HEAD
    this creates an entry point for the command line interpreter
    """
    prompt = "(hbnb)"
    classes = ("BaseModel", "User", "State", "Amenity", "City", "Place", "Review")


    def do_quit(self, line):
=======
    prompt = '(hbnb)'
    classes = ['BaseModel']
    instances = storage.all()

    def do_all(self, arg):
        """_summary_

        Args:
            arg (_type_): _description_
>>>>>>> c76cd43f2ca67d0df5b6a1792b3c70adc94e336b
        """
        classname = parse(arg).get(0)
        instances = self.get_class_instances(classname)
        if instances:
            print(instances)

    def do_create(self, arg):
        """Creates a new instance of `arg`,
        saves it (to the JSON file) and prints the id

        Args:
            arg (str): Name of class to create object
        """
<<<<<<< HEAD
        return True # Return True to indicate that the program should exit
=======
        classname = parse(arg).get(0)
        if self.check_classname(classname):
            obj = BaseModel()
            obj.save()
            print(obj.id)

    def do_show(self, arg):
        """Prints the string representation of an instance based on the class name and id
>>>>>>> c76cd43f2ca67d0df5b6a1792b3c70adc94e336b

        Args:
            arg : strings in the order: classname id
        """
        classname = parse(arg).get(0)
        id = parse(arg).get(1)
        if self.check_classname(classname) and self.check_id(id):
            key = f"{classname}.{id}"
            obj = self.get_instance(key)
            if obj:
                print(obj)

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id
        (save the change into the JSON file)

        Args:
            arg (_type_): _description_
        """
<<<<<<< HEAD
        return True # Return True to indicate that the program should exit
=======
        classname = parse(arg).get(0)
        id = parse(arg).get(1)
        if self.check_classname(classname) and self.check_id(id):
            key = f"{classname}.{id}"
            obj = self.get_instance(key)
            if obj:
                HBNBCommand.instances.pop(key)
                obj.save()

    def do_update(self, arg):
        """ Updates an instance based on the class name and id 
        by adding or updating a single attribute.

        The change is saved into the JSON file.

        Args:
            arg (_type_): _description_
        """
        key = self.get_instance_key(arg)
        obj = self.get_instance(key)
        if obj:

            HBNBCommand.instances.update({key: obj})

    def get_instance_key(self, args):
        """
        """
        classname = parse(args).get(0)
        id = parse(args).get(1)

        if self.check_classname(classname) and self.check_id(id):
            return f"{classname}.{id}"

    def do_EOF(self, arg):
        """Cleanly exits the program on receiving end-of-file marker(Ctrl+D)."""
        return True

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True
>>>>>>> c76cd43f2ca67d0df5b6a1792b3c70adc94e336b

    def emptyline(self):
        pass

    def print_error(self, error_type):
        """Print an error message based on the error type."""
        error_messages = {
            'invalid_class': "** class doesn't exist **",
            'missing_classname': "** class name missing **",
            'missing_id': "** instance id missing **",
            'invalid_id': "** no instance found **",
            'missing_attr_name': "** attribute name missing **",
            'missing_attr_value': "** value missing **"
        }

        print(error_messages.get(error_type, "** unknown error **"))

    def check_classname(self, classname, needed=True):
        """Check if `classname` is a valid class name.

        Args:
            classname(str): name to check if class
            needed (bool): if the classname has to exist or can be None

        Returns:
            bool: True if the class name is valid, False otherwise.
        """

        if needed and classname is None:
            self.print_error('missing_classname')
            return False

        if classname in HBNBCommand.classes:
            return True

        self.print_error('invalid_class')
        return False

    def check_id(self, id):
        """Check if the instance id argument is present.

        Args:
            args (dict): A dictionary containing parsed arguments.

        Returns:
            bool: True if the instance ID is present, False otherwise.
        """
<<<<<<< HEAD
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
=======
        if id is None:
            self.print_error('missing_id')
            return False
>>>>>>> c76cd43f2ca67d0df5b6a1792b3c70adc94e336b

        return True

    def get_instance(self, id):
        """_summary_

        Args:
            id (_type_): _description_
        """
        if id in HBNBCommand.instances:
            return HBNBCommand.instances[id]

        self.print_error('invalid_id')

    def get_class_instances(self, classname=None):
        """Retrieve all instances of a given class or all saved instances
        if no class is specified.

        Args:
            classname (str, optional): Name of the class to retrieve instances for.

        Yields:
            str: Instances as strings.
        """
        if classname is None:
            return [str(obj) for obj in HBNBCommand.instances.values()]

        if self.check_classname(classname, needed=False):
            return [str(v) for k, v in HBNBCommand.instances.items() if k.startswith(classname)]


def parse(arg):
    """Convert console arguments into an argument dict"""

    return {i: val for i, val in enumerate(arg.split())}


<<<<<<< HEAD
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


=======
>>>>>>> c76cd43f2ca67d0df5b6a1792b3c70adc94e336b
if __name__ == '__main__':
    HBNBCommand().cmdloop()
