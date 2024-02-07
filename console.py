"""
This will be the command line interpreter module
"""
import cmd
import json
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    """
    this creates an entry point for the command line interpreter
    """
    def do_quit(self, line):
        """
        console exit command
        """
        return True

    def do_EOF(self, line):
        """
        console exit command
        """
        return True

    def do_create(self, name):
        """
        Creates a new instance of the 'Base Model'
        saves the instance to the JSON file
        Prints the id
        """
        if name:

    def emptyline (self):
        """
        an empty line + ENTER shouldn’t execute anything
        """
        return

