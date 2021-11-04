#!/usr/bin/python3
""" class Base model for AirBnB clone """
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """ Base model 
        id:
        created_at:
        updtaed_at:
    """

    def __init__(self, *args, **kwargs):
        """ Object atributes """

        if len(kwargs) == 0:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.save() 
        else:
            kwargs["created_at"] = datetime.strptime(kwargs["created_at"],
                                   "%Y-%m-%dT%H:%M:%S.%f")
            kwargs["updated_at"] = datetime.strptime(kwargs["updated_at"],
                                   "%Y-%m-%dT%H:%M:%S.%f")

            for key, value in kwargs.items():
                if "__class__" not in key:
                    setattr(self, key, value)

    def __str__(self):
        """ Instance print """
        return "[{:s}] ({:s}) {}".format(self.__class__.__name__, self.id,
                self.__dict__)


    def save(self):
        """ Save changes """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ Dictionary of model """
        dictionary = dict(self.__dict__)
        dictionary['__class__'] = self.__class__.__name__
        dictionary['updated_at'] = self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        dictionary['created_at'] = self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        return dictionary

