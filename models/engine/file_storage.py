import json


class FileStorage:
    ...

    def __init__(self):
        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = f"{obj["__class__"]}.{obj["id"]}"
        self.__objects[key] = obj

    def save(self):
        with open(self.__file_path, "w+") as file:
            json.dump(self.__objects, file, indent=2)

    def reload(self):
        try:
            with open(self.__file_path, "r") as file:
                self.__objects = json.load(file)
        except FileNotFoundError:
            pass
