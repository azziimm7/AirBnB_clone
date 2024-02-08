#!/usr/bin/python3
"""
City Model:
Defines a class City that inherits from BaseModel
    Attributes:
        - state_id (str)
        - name (str)
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    City class representing a city in the AirBnB Clone app.

    Attributes:
        - state_id (str): The ID of the state of the city
        - name (str): The name of the city
    """

    state_id = ""
    name = ""
