#!/usr/bin/python3
"""
A module that contains class that act as BaseModel
"""
import uuid
import datetime
from models import storage

class BaseModel:
    """
    A class that defines the basemodel
    """
    def __init__(self, *args, **kwargs):
        """Initialize instance variables"""
        if kwargs:
            for key, val in kwargs.items():
                if key != '__class__':
                    if key in ['created_at', 'updated_at']:
                        val = datetime.datetime.fromisoformat(val)
                    setattr(self, key, val)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            storage.new(self)

    def __str__(self):
        """Return string representation of class"""
        return ("[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        """Updates the updated_at attribute to current time"""
        self.updated_at = datetime.datetime.now()
        self.updated_at = self.updated_at.isoformat()
        storage.save()

    def to_dict(self):
        """Print dictionary representation of class attriutes and method"""
        my_dict = self.__dict__.copy()
        if isinstance(my_dict['updated_at'], datetime.datetime):
            my_dict['updated_at'] = my_dict['updated_at'].isoformat()
        if isinstance(my_dict['created_at'], datetime.datetime):
            my_dict['created_at'] = my_dict['created_at'].isoformat()
        my_dict['__class__'] = self.__class__.__name__
        return my_dict
    