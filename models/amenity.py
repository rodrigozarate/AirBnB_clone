#!/usr/bin/python3
""" MODULE Amenity for AirBnB clone console """
from models.base_model import BaseModel

class Amenity(BaseModel):
    """ Amenity class """
    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
