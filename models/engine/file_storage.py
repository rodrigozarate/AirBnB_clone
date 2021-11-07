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
            json_obj[key] = self.__objects[key].to_dict()
        with open(self.__file_path, 'w') as file:
            json.dump(json_obj, file, indent=2)

    def reload(self):
        """ deserialize JSON to object """
        try:
            with open(FileStorage.__file_path, mode="r") as file:
                content = file.read()
                dict_from_file = {}
                if content != "":
                    dict_from_file = json.loads(content)

                for file_key, dict_obj in dict_from_file.items():
                    if file_key not in FileStorage.__objects.keys():
                        classFrmt = dict_obj["__class__"]
                        newInstance = eval("{}(**dict_obj)".format(classFrmt))
                        self.new(newInstance)
        except FileNotFoundError:
            pass
