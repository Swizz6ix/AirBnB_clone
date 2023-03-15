#!/usr/bin/python3
"""Defines the Amenity class."""
import os
import sys
import inspect

sys.path.insert(1, os.path.join(sys.path[0], '..'))
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Represent an amenity.
    Attributes:
        name (str): The name of the amenity.
    """

    name = ""
