#!/usr/bin/python3
""" Unitest for console """
import unittest
import sys
import re
import random
from io import StringIO
from console import HBNBCommand
from models import *
from unittest.mock import patch


class TestConsole(unittest.TestCase):
    """ Main class to test console """
    def test_help(self):
        expected = """
Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update
\n"""
        with patch('sys.stdout', new=StringIO()) as str:
            HBNBCommand().onecmd("help")
            self.assertEqual(expected, str.getvalue())
