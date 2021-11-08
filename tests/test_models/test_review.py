#!/usr/bin/python3
""" Unittest review model """
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.review import Review


class TestReview_instantiation(unittest.TestCase):
    """ Unittests instantiation Review """

    def test_no_args_instantiates(self):
        self.assertEqual(Review, type(Review()))
