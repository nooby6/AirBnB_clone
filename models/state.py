#!/usr/bin/python3
"""This module defines the class State"""

from models.base_model import BaseModel


class State(BaseModel):
    """This class defines a State(geographical division)"""

    name = ''

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
