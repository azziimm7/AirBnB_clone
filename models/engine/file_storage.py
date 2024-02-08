#!/usr/bin/python3
"""
File Storage Module:
Defines the FileStorage class responsible for serializing and deserializing.

Attributes:
    - __file_path (str): The path to the JSON file where instances are stored
    - __objects (dict): A dictionary to store instances
    - __allclass (dict): A dictionary mapping class names to their classes

Methods:
    - all(self): Returns the dictionary of all stored instances
    - new(self, obj): Adds a new instance to the dictionary
    - save(self): Serializes instances to JSON and saves them to the file
    - reload(self): Deserializes JSON from the file and loads instances
"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """
    FileStorage class responsible for
    serializing and deserializing instances
    to and from JSON files.
    """

    def __init__(self):
        """Initializes the FileStorage instance"""

        self.__file_path = "file.json"
        self.__objects = {}
        self.__allclass = {
                "BaseModel": BaseModel,
                "User": User,
                "State": State,
                "City": City,
                "Amenity": Amenity,
                "Place": Place,
                "Review": Review
            }

    def all(self):
        """Returns: A dictionary containing all stored instances"""

        return self.__objects

    def new(self, obj):
        """
        Adds a new instance to the dictionary

        Args:
            - obj: The instance to add.
        """

        objclsname = obj.__class__.__name__
        self.__objects["{}.{}".format(objclsname, obj.id)] = obj

    def save(self):
        """Serializes instances to JSON and saves them to the file"""

        objdict = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, 'w') as f:
            json.dump(objdict, f)

    def reload(self):
        """Deserializes JSON from the file and loads instances into memory"""

        try:
            with open(self.__file_path, 'r') as f:
                info = json.load(f)
                for key, value in info.items():
                    classname, obj_id = key.split(".")
                    if classname in self.__allclass:
                        classobj = self.__allclass[classname]
                        instance = classobj(**value)
                        self.__objects[key] = instance
        except FileNotFoundError:
            return
