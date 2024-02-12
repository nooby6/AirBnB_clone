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
        self.cmd = HBNBCommand()

    def tearDown(self):
        """Tear down test fixtures."""
        self.cmd =none
        pass

    def test_quit_command(self):
        """Test quit command."""
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.assertTrue(self.console.onecmd("quit"))
            self.assertEqual(fake_out.getvalue().strip(), "Exiting the program...")
            output = fake_out.getvalue().strip()
            self.assertEqual(output, '')

    def test_EOF_command_success(self):

    def test_emptyline_command(self)

if __name__ == '__main__':
    unittest.main()
