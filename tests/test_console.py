#!/usr/bin/python3
"""This module contains unit tests for the console"""
import unittest
from console import HBNBCommand
from unittest.mock import patch
from io import StringIO

class TestConsole(unittest.TestCase):
    """This class defines a couple of tests for the console.
    """

    def setUp(self):
        """Set up test fixtures"""
        self.console = HBNBCommand()

    def tearDown(self):
        """Tear down test fixtures"""
        pass

    def test_quit_command(self):
        """Test quit command"""
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.assertTrue(self.console.onecmd("quit"))
            self.assertEqual(fake_out.getvalue().strip(), "Exiting the program...")

    def test_create_command(self):
        """Test create command"""
        # Implement test cases for create command

    def test_show_command(self):
        """Test show command"""
        # Implement test cases for show command

    def test_destroy_command(self):
        """Test destroy command"""
        # Implement test cases for destroy command

    def test_all_command(self):
        """Test all command"""
        # Implement test cases for all command

    def test_update_command(self):
        """Test update command"""
        # Implement test cases for update command

if __name__ == '__main__':
    unittest.main()
