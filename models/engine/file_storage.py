#!/usr/bin/python3
"""This module defines a class for JSON serialization/deserialization"""

import json

class FileStorage():
    """Serializes all instances of BaseClass to a JSON file and
    deserializes a JSON file to BaseModel instances.
    """
    __file_path = 'file.json'
    __objects = dict()

    def __init__(self) -> None:
        pass

    def all(self) -> dict:
        """Returns all instances of the BaseModel class

        Returns:
            dict: Dictionary of <classname>.id : object.to_dict
        """

        return FileStorage.__objects

    def new(self, obj):
        """Adds a new object to the class' `__objects`

        Args:
            obj : a BaseModel object dictionary
        """
        from models.base_model import BaseModel

        if isinstance(obj, dict):
            obj = BaseModel(**obj)

        obj_key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects.update({obj_key: obj})

    def save(self):
        """Serializes the class' `__objects` to a JSON file.
        (path: __file_path)
        """
        objs = self.all()
        json_str = json.dumps({key: obj.to_dict()
                              for key, obj in objs.items()})

        with open(FileStorage.__file_path, 'w', encoding='utf-8') as f:
            f.write(json_str)

    def reload(self):
        """Deserializes the JSON file to __objects,
        only if the JSON file (__file_path) exists
        """

        try:
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as f:
                json_str = f.read()
                if not json_str:
                    return
                json_objs = json.loads(json_str)
                for obj_dict in json_objs.values():
                    self.new(obj_dict)
        except FileNotFoundError:
            pass
