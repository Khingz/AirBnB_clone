#!/usr/bin/python3
"""
A file that contains the class for filestorage
"""

import json

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
            self.__objects[key] = obj.to_dict()

    def save(self):
        """
        serializes object to json file
        """
        with open(self.__file_path, 'w') as f:
            js = json.dumps(self.__objects)
            f.write(js)

    def reload(self):
        """
        deserializes json file to object
        """
        try:
            with open(self.__file_path, 'r') as f:
                js = f.read()
                if js:
                    self.__objects = json.loads(js)
                else:
                    self.__objects = {}
        except FileNotFoundError:
            pass