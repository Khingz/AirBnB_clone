#!/usr/bin/python3
"""
A file that contains the class for filestorage
"""

import json
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State

class FileStorage():
    """
    File storage class
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        returns dictionary of object stored in file
        """
        return self.__objects

    def new(self, obj):
        """
        sets a new object to the __object dict
            Args:
                obj: object to be set
        """
        if obj:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            FileStorage.__objects[key] = obj

    def save(self):
        """
        serializes object to json file
        """
        with open(self.__file_path, 'w') as f:
            store = FileStorage.__objects
            de_ob = {k: v.to_dict() for k, v in store.items()}
            json.dump(de_ob, f)

    def reload(self):
        """
        deserializes json file to object
        """
        __classes = {
            "BaseModel": BaseModel,
            "User": User,
            "Amenity": Amenity,
            "City": City,
            "Place": Place,
            "Review": Review,
            "State": State
        }

        try:
            path = FileStorage.__file_path
            store = FileStorage.__objects
            with open(path, 'r') as f:
                loaded_ob = json.load(f)
                for k, v in loaded_ob.items():
                    cls = v['__class__']
                    store[k] = __classes[cls](**v)
        except FileNotFoundError:
            pass