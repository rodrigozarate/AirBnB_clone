#!/usr/bin/python3
""" unittest city model """
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.city import City


class TestCity_instantiation(unittest.TestCase):
    """ Unittests instantiation City """

    def test_no_args_instantiates(self):
        self.assertEqual(City, type(City()))
