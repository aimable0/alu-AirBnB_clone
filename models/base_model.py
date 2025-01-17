#!/usr/bin/python3

from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """_summary_

    Returns:
        _type_: _description_
    """

    # public instances
    def __init__(self, *args, **kwargs):
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key == "updated_at":
                        setattr(self, key, datetime.fromisoformat(value))
                    elif key == "created_at":
                        setattr(self, key, datetime.fromisoformat(value))
                    else:
                        setattr(self, key, value)

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    # public methods.
    def save(self):
        """updates attribute 'updated_at' with the current datetime"""
        self.updated_at = datetime.today()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """returns a dict containing all keys/values of the instance"""
        instance_dict = self.__dict__.copy()
        instance_dict["updated_at"] = self.updated_at.isoformat()
        instance_dict["created_at"] = self.created_at.isoformat()
        instance_dict["__class__"] = self.__class__.__name__
        return instance_dict
