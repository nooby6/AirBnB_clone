#!/usr/bin/python3
"""This module defines the class Amenity"""

from models.base_model import BaseModel

class Amenity(BaseModel):
    """This class defines an anemity that can be found in a place"""

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        if kwargs:
            Amenity.create_from_kwargs(self, kwargs)
        else:
            self.name = ''
