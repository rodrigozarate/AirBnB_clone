#!/usr/bin/python3
""" MODULE user for AirBnB clone console """
from models.base_model import BaseModel


class User(BaseModel):
    """ User class """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
