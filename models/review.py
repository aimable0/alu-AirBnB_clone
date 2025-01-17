#!/usr/bin/python3

from models_base import BaseModel


class Review(BaseModel):
    """_summary_

    Args:
        BaseModel (_type_): _description_
    """

    place_id: str = ""  # it will be the Place.id
    user_id: str = ""  # it will be the User.id
    text: str = ""
