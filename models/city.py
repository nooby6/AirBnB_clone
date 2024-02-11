#!/usr/bin/python3
"""This module defines the class City"""

from models.base_model import BaseModel


class City(BaseModel):
    """This class defines a city within a state"""

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        if kwargs:
            City.create_from_kwargs(self, kwargs)
        else:
            self.state_id = ''
            self.name = ''
