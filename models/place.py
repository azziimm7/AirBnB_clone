#!/usr/bin/python3
"""
Place Model:
Defines a class Place that inherits from BaseModel
    Attributes:
        - city_id (str)
        - user_id (str)
        - name (str)
        - description (str)
        - number_rooms (int)
        - number_bathrooms (int)
        - max_guest (int)
        - price_by_night (int)
        - latitude (float)
        - longitude (float)
        - amenity_ids (list)
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """
    Place class representing a place in the AirBnB Clone app.

    Attributes:
        - city_id (str): The ID of the city.
        - user_id (str): The ID of the user.
        - name (str): The name of the place.
        - description (str): A description of the place.
        - number_rooms (int): The number of rooms.
        - number_bathrooms (int): The number of bathrooms.
        - max_guest (int): The maximum number of guests.
        - price_by_night (int): The price per night to stay.
        - latitude (float): The latitude coordinate of the place.
        - longitude (float): The longitude coordinate of the place.
        - amenity_ids (list): A list of IDs of amenities available.
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
