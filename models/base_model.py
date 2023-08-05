#!/usr/bin/python3
"""
A module that contains class that act as BaseModel
"""
import uuid
import datetime

class BaseModel:
    """
    A class that defines the basemodel
    """
    def __init__(self):
        """Initialize instance variables"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        """Return string representation of class"""
        return ("{}, {}".format(self.updated_at, self.id))
    
    def save(self):
        """Updates the updated_at attribute to current time"""
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """Print dictionary representation of class attriutes and method"""
        pass