#!/usr/bin/python3
""" Model storage serialize and deserialization """
import json
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class FileStorage:
    """ save the data to file """

    __file_path = "data.json"
    __objects = {}

    def all(self):
        """ return dictionary objects """
        return self.__objects

    def new(self, obj):
        """ set objects with keys """
        names = obj.to_dict()
        keys = "{}.{}".format(names["__class__"], names["id"])
        self.__objects[keys] = obj

    def save(self):
        """ serializes to JSON """
        json_obj = {}
        for key in self.__objects:
            json_obj[key] = self._objects[key].to_dict()
        with open(self.__file_path, 'w') as file:
            json.dump(json_obj, file, indent=2)

    def reload(self):
        """ deserialize JSON to object """
