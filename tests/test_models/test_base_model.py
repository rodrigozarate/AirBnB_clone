#!/usr/bin/python3
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.base_model import BaseModel


class TestBaseModel_instantiation(unittest.TestCase):
    """ Unittests instantiation BaseModel """

    def test_no_args_instantiates(self):
        self.assertEqual(BaseModel, type(BaseModel()))
