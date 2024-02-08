#!/usr/bin/python3
"""
Review Model:
Defines a class Review that inherits from BaseModel
    Attributes:
        - place_id (str)
        - user_id (str)
        - text (str)
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Review class representing a review in the AirBnB Clone app.

    Attributes:
        - place_id (str): The ID of the place associated with the review.
        - user_id (str): The ID of the user who wrote the review.
        - text (str): The text content of the review.
    """

    place_id = ""
    user_id = ""
    text = ""
