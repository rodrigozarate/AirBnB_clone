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

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ return dictionary objects """
        return FileStorage.__objects

    def new(self, obj):
        """ set objects with keys """
        names = obj.to_dict()
        keys = "{}.{}".format(names["__class__"], names["id"])
        FileStorage.__objects[keys] = obj

    def save(self):
        """ serializes to JSON """
        prev_dict = FileStorage.__objects
        new_dict = {obj: prev_dict[obj].to_dict() for obj in prev_dict.keys()}
        with open(FileStorage.__file_path, 'w') as file:
            json.dump(new_dict, file)

    def reload(self):
        """ deserialize JSON to object """
        try:
            with open(FileStorage.__file_path) as file:
                content = json.load(file)
                for file_key in content.values():
                    class_name = file_key["__class__"]
                    del file_key["__class__"]
                    self.new(eval(class_name)(**file_key))
        except FileNotFoundError:
            return
