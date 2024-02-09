#!/usr/bin/python3
"""This module defines the class User"""

from models.base_model import BaseModel


class User(BaseModel):
    """This class describes a user."""

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        if kwargs:
            User.create_from_kwargs(self, kwargs)
        else:
            self.email = ''
            self.password = ''
            self.first_name = ''
            self.last_name = ''
