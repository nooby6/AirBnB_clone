#!/usr/bin/python3
"""
This will be the command line interpreter module
"""
import cmd
from models import storage
import re


class HBNBCommand(cmd.Cmd):
    """This class defines a console for managing objects.

    Has create, show, update and delete functionality.
    """
    prompt = "(hbnb)"
    classes = ("BaseModel", "User", "State", "Amenity", "City", "Place", "Review")

    def precmd(self, line: str) -> str:
        """Converts a <classname>.command(arguments) command to the standard
        command ClassName arguments format.

        Args:
            line (str): Initial command

        Returns:
            str: Converted command
        """
        pattern = r'(\w+)\.(\w+)\((.*)\)'

        match = re.search(pattern, line)

        if match:
            class_name = match.group(1)
            method_name = match.group(2)
            args = (' ').join(m.strip() for m in match.group(3).split(','))

            line = f"{method_name} {class_name} {args}"

        return super().precmd(line)

    def do_all(self, arg):
        """Prints a list of all instances of a class or
        of all classes if no class is specified

        Args:
            arg (str): class to display objects of
        """
        classname = parse(arg).get('class')
        if check_classname(classname, needed=False):
            instances = storage.get_class_instances(classname)
            print(instances)

    def do_create(self, arg):
        """Creates a new instance of `arg`,
        saves it (to the JSON file) and prints the id

        Args:
            arg (str): Name of class to create object
        """
        classname = parse(arg).get('class')
        if check_classname(classname):
            obj = storage.create_new(classname)
            obj.save()
            print(obj.id)

    def do_show(self, arg):
        """Prints the string representation of an instance based on the class name and id

        Args:
            arg (str): class and object id in the order: `classname id`
        """
        key = get_instance_key(parse(arg))
        if key:
            obj = storage.get_instance(key)
            print(obj or error('invalid_id'))

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id
        (save the change into the JSON file)

        Args:
            arg (str): class and object id in the order: `classname id`
        """

        key = get_instance_key(parse(arg))
        if key:
            if not storage.destroy_instance(key):
                print(error('invalid_id'))

    def do_update(self, arg):
        """ Updates an instance based on the class name and id
        by adding or updating a single attribute.

        The change is saved into the JSON file.

        Args:
            arg (str): class, object id and atribbute in the order:
            `classname id attribute_name attribute_value`
        """
        key = get_instance_key(parse(arg))
        attr_name = parse(arg).get('attr_name')
        attr_value = parse(arg).get('attr_val')
        if check_attributes(attr_name, attr_value):
            storage.update_instance(key, attr_name, attr_value)

    def do_count(self, arg):
        """_summary_

        Args:
            arg (_type_): _description_
        """
        classname = parse(arg).get('class')
        if check_classname(classname, needed=True):
            instances = storage.get_class_instances(classname)
            print(len(instances))

    def do_EOF(self, arg):
        """Cleanly exits the program on receiving end-of-file marker(Ctrl+D).
        """
        return True

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_help(self, args):
        """
        List available commands with "help" or detailed help with "help cmd"
        """
        # Call the  do_help method of the parent class to provide default behaviour
        cmd.Cmd.do_help(self, args)
        
    def emptyline(self):
        pass


def error(error_type):
    """Return an error message based on the error type."""
    error_messages = {
        'invalid_class': "** class doesn't exist **",
        'missing_classname': "** class name missing **",
        'missing_id': "** instance id missing **",
        'invalid_id': "** no instance found **",
        'missing_attr_name': "** attribute name missing **",
        'missing_attr_value': "** value missing **"
    }

    return error_messages.get(error_type, "** unknown error **")


def check_classname(classname, needed=True):
    """Check if `classname` is a valid class name.

    Args:
        classname(str): name to check if class
        needed (bool): if the classname has to exist or can be None

    Returns:
        bool: True if the class name is valid, False otherwise.
    """
    classes = ['BaseModel', 'User', 'State',
               'City', 'Amenity', 'Place', 'Review']

    if classname is None and not needed:
        return True

    if classname is None and needed:
        print(error('missing_classname'))
        return False

    if classname in classes:
        return True

    print(error('invalid_class'))
    return False


def check_id(id):
    """Check if the instance id argument is present.

    Args:
        args (dict): A dictionary containing parsed arguments.

    Returns:
        bool: True if the instance ID is present, False otherwise.
    """
    if id is None:
        print(error('missing_id'))
        return False

    return True


def check_attributes(attr_name, attr_value):
    """Verifies that the attribute name  and value exist and are valid

    Args:
        args (str): Attribute to verify
    """
    if attr_name is None:
        print(error('missing_attr_name'))
        return False

    if attr_name in ['id', 'created_at', 'updated_at']:
        return False

    if attr_value is None:
        print(error('missing_attr_value'))
        return False

    return True


def get_instance_key(args):
    """
    """
    classname = args.get('class')
    id = args.get('id')

    if check_classname(classname) and check_id(id):
        return f"{classname}.{id}"


def parse(arg):
    """Convert console arguments into an argument dict"""
    args = ['class', 'id', 'attr_name', 'attr_val']

    return dict(zip(args, arg.split()))

if __name__ == '__main__':
    HBNBCommand().cmdloop()
