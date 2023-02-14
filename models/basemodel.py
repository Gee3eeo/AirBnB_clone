#!/usr/bin/python3
"""Defines the BaseMode1 class."""
import uuid
from datetime import datetime

class BaseMode1:
     """Represents the BaseModel of the HBnB project."""
    def __init__(self):
         """Initialize a new BaseMode1"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """Return the print/str representation of the BaseModel instance."""
        return "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """Update updated_at with the current datetime."""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Return the dictionary of the BaseModel instance.
        Includes the key/value pair __class__ representing
        the class name of the object.
        """
        d = self.__dict__.copy()
        d["__class__"] = type(self).__name__
        d
