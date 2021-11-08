#!/usr/bin/python3
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.user import User


class TestUser_instantiation(unittest.TestCase):
    """Unittests instantiation User """

    def test_no_args_instantiates(self):
        self.assertEqual(User, type(User()))
