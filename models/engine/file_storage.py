#!/usr/bin/python3
"""
A file that contains the class for filestorage
"""

class FileStorage():
    """
    File storage class
    """
    def __init__(self):
        """init function for the file storage class"""
        pass

    def all(self):
        """
        returns dictionary of object stored in file
        """
        pass

    def new(self, obj):
        """
        sets a new object to the __object dict
            Args:
                obj: object to be set
        """
        pass

    def save(self):
        """
        serializes object to json file
        """
        pass

    def reload(self):
        """
        deserializes json file to object
        """
        pass