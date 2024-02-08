#!/usr/bin/python3
"""This module defines the class Review"""

from models.base_model import BaseModel


class Review(BaseModel):
    """This class defines a review of a place left by a user"""

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        if kwargs:
            self = Review.create_from_kwargs(kwargs)
        else:
            self.place_id = ''
            self.user_id = ''
            self.text = ''
