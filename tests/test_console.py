#!/usr/bin/env python3
"""Module containing unit tests for the console."""
import unittest
from console import HBNBCommand
from unittest.mock import patch
from io import StringIO


class TestConsole(unittest.TestCase):
    """Class defining tests for the console."""

    def setUp(self):
        """Set up test fixtures."""
        self.console = HBNBCommand()

    def tearDown(self):
        """Tear down test fixtures."""
        pass

    def test_quit_command(self):
        """Test quit command."""
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.assertTrue(self.console.onecmd("quit"))
            self.assertEqual(fake_out.getvalue().strip(), "Exiting the program...")

    def test_create_command(self):
        """Test create command."""
        # Write test cases for create command
        pass

    def test_show_command(self):
        """Test show command."""
        # Write test cases for show command
        pass

    def test_destroy_command(self):
        """Test destroy command."""
        # Write test cases for destroy command
        pass

    def test_all_command(self):
        """Test all command."""
        # Write test cases for all command
        pass

    def test_update_command(self):
        """Test update command."""
        # Write test cases for update command
        pass


if __name__ == '__main__':
    unittest.main()
