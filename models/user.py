#!/usr/bin/python3
"""A file that houses the User class"""

from models.base_model import BaseModel


class User(BaseModel):
    """
    Class that defines the User
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
