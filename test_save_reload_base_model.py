#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel

# all_objs = storage.all()
# print("-- Reloaded objects --")
# for obj_id in all_objs.keys():
#     obj = all_objs[obj_id]
#     print(obj)

# print("-- Create a new object --")
# my_model = BaseModel()
# my_model.name = "My_First_Model"
# my_model.my_number = 89
# my_model.save()
# print(my_model)

# print(type(all_objs) == dict)

instance = BaseModel()
storage.new(instance)
assert instance in (storage._FileStorage__objects).keys()
print(type(storage._FileStorage__objects))
for i in storage._FileStorage__objects:
    if str(i).endswith(instance.id):
        print(i)