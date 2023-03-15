#!/usr/bin/python3
"""Defines the State class."""
import os
import sys
import inspect

sys.path.insert(1, os.path.join(sys.path[0], '..'))
from models.base_model import BaseModel


class State(BaseModel):
    """Represent a state.
    Attributes:
        name (str): The name of the state.
    """

    name = ""
