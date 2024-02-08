#!/usr/bin/python3
"""
State Model:
Defines a class State that inherits from BaseModel
    Attributes:
        - name (str)
"""
from models.base_model import BaseModel


class State(BaseModel):
    """
    State class representing a state in the AirBnB Clone app.

    Attributes:
        - name (str): The name of the state
    """
    name = ""
