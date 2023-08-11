#!/usr/bin/python3
"""A file that houses the Review class"""

from models.base_model import BaseModel


class Review(BaseModel):
    """
    Class that defines the Review
    """
    place_id = ""
    user_id = ""
    text = ""
