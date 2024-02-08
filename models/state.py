#!/usr/bin/python3
"""This module defines the class State"""

from models.base_model import BaseModel


class State(BaseModel):
    """This class defines a State(geographical division)"""

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        if kwargs:
            self = State.create_from_kwargs(kwargs)
        else:
            self.name = ''
