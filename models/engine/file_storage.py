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
        if isinstance(obj, dict):
            obj = self.create_new(obj['__class__'], obj)

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

    def create_new(self, classname, args=None):
        """Create a new instance of the specified class.

        Args:
            classname (str): The name of the class to instantiate.
        """
        
        # Dynamically import the class
        class_map = {'BaseModel': 'base_model',
                     'User': 'user',
                     'Place': 'place',
                     'Amenity': 'amenity',
                     'State': 'state',
                     'City': 'city',
                     'Review': 'review'}

        file_name = class_map.get(classname)
        module = __import__(f"models.{file_name}", fromlist=[classname])

        cls = getattr(module, classname)  

        if args:        
            return cls(**args)
        
        return cls()
    
    def get_instance(self, key):
        """_summary_

        Args:
            id (_type_): _description_
        """
        
        return self.__objects.get(key)

    def destroy_instance(self, key):
        """_summary_

        Args:
            key (_type_): _description_
        """

        if key in self.__objects:
            self.__objects.pop(key)
            self.save()
            return True
        
    def get_class_instances(self, classname=None):
        """Retrieve all instances of a given class or all saved instances
        if no class is specified.

        Args:
            classname (str, optional): Name of the class to retrieve instances for.

        Returns:
            list[str]: Instances as strings.
        """
        if classname is None:
            return [str(obj) for obj in self.__objects.values()]
        
        return [str(v) for k, v in self.__objects.items() if k.startswith(classname)]

    def update_instance(self, obj_key, attr_name, attr_val):
        """_summary_

        Args:
            obj_key (_type_): _description_
            attr_name (_type_): _description_
            attr_val (_type_): _description_
        """
        obj = self.get_instance(obj_key)
        if obj:            
            attr_type = type(getattr(obj, attr_name, ''))
            attr_val = attr_type(attr_val)
            setattr(obj, attr_name, attr_val)

    