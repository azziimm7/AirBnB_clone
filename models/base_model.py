#!/usr/bin/python3
"""
Base Model class Module
    contains BaseModel class: base class for all models in the AirBnB Clone app

    Attributes:
        - id (str): Ensures that each instance of BaseModel
        has a distinct identifier.
        - created_at (datetime): Keeps track of when an instance was created.
        - updated_at (datetime): Keeps track of the last modification time.
    Methods:
        - __str__: [<class name>] (<self.id>) <self.__dict__>
        - save(self): Updates the public instance attribute
        updated_at with the current datetime.
        - to_dict(self): Creates a dictionary representation of the object.
"""
import models
import uuid
from datetime import datetime


class BaseModel:
    """ """
    def __init__(self, *args, **kwargs):
        """ """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        models.storage.new(self)

        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key in ["created_at", "updated_at"]:
                        self.__dict__[key] = datetime.strptime(
                                value, "%Y-%m-%dT%H:%M:%S.%f")
                    else:
                        self.__dict__[key] = value
        models.storage.new(self)

    def __str__(self):
        """ """
        classname = self.__class__.__name__
        return "[{}] ({}) {}".format(classname, self.id, self.__dict__)

    def save(self):
        """ """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ """
        info = self.__dict__.copy()
        info["__class__"] = self.__class__.__name__
        info["created_at"] = self.created_at.isoformat()
        info["updated_at"] = self.updated_at.isoformat()
        return info
