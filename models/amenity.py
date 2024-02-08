#!/usr/bin/python3
"""
Amenity Model:
Defines a class Amenity that inherits from BaseModel
    Attributes:
        - name (str)
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Amenity class representing an amenity in the AirBnB Clone app.

    Attributes:
        - name (str): The name of the amenity
    """

    name = ""
