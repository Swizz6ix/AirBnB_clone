#!/usr/bin/python3
"""Defines the City class."""
import os
import sys
import inspect

sys.path.insert(1, os.path.join(sys.path[0], '..'))
from models.base_model import BaseModel


class City(BaseModel):
    """Represent a city.
    Attributes:
        state_id (str): The state id.
        name (str): The name of the city.
    """

    state_id = ""
    name = ""
