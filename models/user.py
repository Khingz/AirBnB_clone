#!/usr/bin/python3
"""A file that houses the User class"""

from models.base_model import BaseModel

class User(BaseModel):
    """
    Class that defines the User
    """
    def __init__(self, *args, **kwargs):
        """Init function for user class"""
        super().__init__(*args, **kwargs)
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""