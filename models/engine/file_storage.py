#!/usr/bin/python3
"""
A file that contains the class for filestorage
"""

import json
from models.base_model import BaseModel
from models.user import User

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
            "User": User
        }

        try:
            path = FileStorage.__file_path
            store = FileStorage.__objects
            with open(path, 'r') as f:
                js = f.read()
                if js:
                    loaded_ob = json.loads(js)
                    for k, v in loaded_ob.items():
                        cls = v['__class__']
                        store[k] = __classes[cls](**v)
                else:
                    return
        except FileNotFoundError:
            pass