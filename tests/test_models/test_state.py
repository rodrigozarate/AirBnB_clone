#!/usr/bin/python3
""" Unittest for state module """
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.state import State


class TestState_instantiation(unittest.TestCase):
    """ Unittests instantiation State """

    def test_no_args_instantiates(self):
        self.assertEqual(State, type(State()))
