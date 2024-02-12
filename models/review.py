#!/usr/bin/python3
"""This module defines the class Review"""

from models.base_model import BaseModel


class Review(BaseModel):
    """This class defines a review of a place left by a user"""

    place_id = ''
    user_id = ''
    text = ''

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
