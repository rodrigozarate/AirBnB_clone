#!/usr/bin/python3
""" MODULE user for AirBnB clone console """
from models.base_model import BaseModel

class User(BaseModel):
    """ User class """
    first_name = ""
    last_name = ""
    email = ""
    password = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
