#!/usr/bin/python3
"""
User Model:
defines a class User that inherits from BaseModel
    Attributes:
        - email (str)
        - password (str)
        - first_name (str)
        - last_name (str)
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    User class representing a user in the AirBnB Clone app

    Attributes:
        - email (str): The email address of the user
        - password (str): The password of the user
        - first_name (str): The first name of the user
        - last_name (str): The last name of the user
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
