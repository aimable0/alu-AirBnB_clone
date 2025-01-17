#!/usr/bin/python3
import json


class FileStorage:
    ...

    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = f'{obj.to_dict()["__class__"]}.{obj.to_dict()["id"]}'
        self.__objects[key] = obj

    def save(self):
        json_objects = {}
        for key in self.__objects.keys():
            json_objects[key] = self.__objects[key].to_dict()
        with open(self.__file_path, "w") as file:
            json.dump(json_objects, file)

    def reload(self):
        try:
            with open(self.__file_path, "r") as file:
                obj_dict = json.load(file)
                from models.base_model import BaseModel
                from models.user import User

                for key in obj_dict:
                    if str(key).startswith("BaseModel"):
                        self.__objects[key] = BaseModel(**obj_dict[key])
                    elif str(key).startswith("User"):
                        self.__objects[key] = User(**obj_dict[key])
        except FileNotFoundError:
            pass

    def delete(self, key):
        """delete an instance and save changes to storage file"""
        self.__objects.__delitem__(key)
        self.save()
