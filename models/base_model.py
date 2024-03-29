#!/usr/bin/python3
"""This module defines a base class for all other classes in this project"""

from datetime import datetime
from models import storage
from uuid import uuid4


class BaseModel():
    """Base class holding properties and methods used by
    all other inheriting classes.
    """

    date_fields = ['created_at', 'updated_at']

    def __init__(self, *args, **kwargs) -> None:
        """Initialize class object instances.

        If `**kwargs` exists, the values will be used to initiliaze the object,
        otherwise sets `id` and `created_at`.
        """
        if kwargs:
            BaseModel.create_from_kwargs(self, kwargs)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    @classmethod
    def create_from_kwargs(cls, obj, kwargs):
        """Sets attributes of an instance of the calling class
        from a dictionary of arguments

        Args:
            obj : instance
            kwargs : keyword arguments corresponding to attributes
        """
        attrs = [k for k in kwargs.keys() if k != '__class__']
        for k in attrs:
            if k in BaseModel.date_fields:
                setattr(obj, k, datetime.fromisoformat(kwargs[k]))
                continue
            setattr(obj, k, kwargs[k])

    def save(self):
        """Saves objects of this class to file.

        Calls the `save` method of the `FileStorage` class.
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Returns a dictionary representation of the object.

        The datetime fields are formatted as ISO strings and
        an extra field `__class__` is included
        """
        obj_dict = vars(self).copy()
        obj_dict.setdefault('__class__', self.__class__.__name__)
        obj_dict.update({f: obj_dict[f].isoformat() for f in self.date_fields})

        return obj_dict

    def __str__(self):
        """Returns the string representation of an instance of this class
        in the format: `[<class name>] (<self.id>) <self.__dict__>`
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
