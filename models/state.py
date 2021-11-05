#!/usr/bin/python3
""" MODULE state for AirBnB clone console """
from models.base_model import BaseModel

class State(BaseModel):
    """ Amenity class """
    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
