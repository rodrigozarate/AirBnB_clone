#!/usr/bin/python3
""" MODULE city for AirBnB clone console """
from models.base_model import BaseModel

class City(BaseModel):
    """ Amenity class """
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
