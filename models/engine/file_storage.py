#!/usr/bin/python3
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


classes = {
    "BaseModel": BaseModel,
    "User": User,
    "State": State,
    "City": City,
    "Amenity": Amenity,
    "Place": Place,
    "Review": Review,
}


class FileStorage:
    ...

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = f'{obj.to_dict()["__class__"]}.{obj.to_dict()["id"]}'
        self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        json_objects = {}
        for key in self.__objects.keys():
            json_objects[key] = self.__objects[key].to_dict()
        with open(self.__file_path, "w") as file:
            json.dump(json_objects, file)

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, "r") as file:
                obj_dict = json.load(file)
                # from models.base_model import BaseModel
                # from models.user import User
                for key in obj_dict:
                    self.__objects[key] = classes[obj_dict[key]["__class__"]](
                        **obj_dict[key]
                    )
                # for key in obj_dict:
                #     if str(key).startswith("BaseModel"):
                #         self.__objects[key] = BaseModel(**obj_dict[key])
                #     elif str(key).startswith("User"):
                #         self.__objects[key] = User(**obj_dict[key])
        except FileNotFoundError:
            pass

    def delete(self, key):
        """delete an instance and save changes to json file"""
        self.__objects.__delitem__(key)
        self.save()
