#!/usr/bin/python3

from models.base_model import BaseModel


class City(BaseModel):
    """_summary_

    Args:
        BaseModel (_type_): _description_
    """

    state_id: str = ""  # it will be the state.id
    name: str = ""
