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

                for key in obj_dict:
                    self.__objects[key] = BaseModel(**obj_dict[key])
        except FileNotFoundError:
            pass

