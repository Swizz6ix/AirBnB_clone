#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State

all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

print("-- Create a new User --")
my_user = User()
my_user.first_name = "ObaLola"
my_user.last_name = "King"
my_user.email = "kingoba@mail.com"
my_user.password = "obasco"
my_user.save()
print(my_user)

print("-- Create a new User 2 --")
my_user2 = User()
my_user2.first_name = "Panama"
my_user2.last_name = "Chike"
my_user2.email = "panachike@mail.com"
my_user2.password = "PanaTime"
my_user2.save()
print(my_user2)