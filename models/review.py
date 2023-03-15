#!/usr/bin/python3
"""Defines the Review class."""
import os
import sys
import inspect

sys.path.insert(1, os.path.join(sys.path[0], '..'))
from models.base_model import BaseModel


class Review(BaseModel):
    """Represent a review.
    Attributes:
        place_id (str): The Place id.
        user_id (str): The User id.
        text (str): The text of the review.
    """

    place_id = ""
    user_id = ""
    text = ""
