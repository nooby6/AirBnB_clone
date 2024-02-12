#!/usr/bin/python3
"""This module defines the class User"""

from models.base_model import BaseModel


class User(BaseModel):
    """This class describes a user."""

    email = ''
    password = ''
    first_name = ''
    last_name = ''

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
