#!/usr/bin/python3
""" unittest for model place """
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.place import Place


class TestPlace_instantiation(unittest.TestCase):
    """ Unittests instantiation Place """

    def test_no_args_instantiates(self):
        self.assertEqual(Place, type(Place()))
