#!/usr/bin/python3
from models.base_model import BaseModel


class User(BaseModel):
    """create a user"""

    # public attributes of a user
    email = ""
    password = ""
    first_name = ""
    last_name = ""