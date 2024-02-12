#!/usr/bin/python3
"""This module defines the class City"""

from models.base_model import BaseModel


class City(BaseModel):
    """This class defines a city within a state"""

    state_id = ''
    name = ''

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
