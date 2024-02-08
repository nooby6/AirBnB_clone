#!/usr/bin/python3
"""This module defines the class Amenity"""

from models.base_model import BaseModel

class Amenity(BaseModel):
    """This class defines an anemity that can be found in a place"""

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        if kwargs:
            self = Amenity.create_from_kwargs(kwargs)
        else:
            self.name = ''
