#!/usr/bin/python3

import unittest
from models.user import User
from models.base_model import BaseModel
from models import storage


class TestUser(unittest.TestCase):
    """test class User"""

    def setUp(self):
        self.instance = User()

    # def tearDown(self):
    #     self.key = self.instance.__class__.__name__ + "." + str(self.instance.id)
    #     storage.delete(self.key)

    def test_user(self):
        self.assertTrue(issubclass(User, BaseModel))
        self.assertIsInstance(self.instance, BaseModel)
        self.assertTrue(hasattr(self.instance, "id"))
        self.assertTrue(hasattr(self.instance, "created_at"))
        self.assertTrue(hasattr(self.instance, "updated_at"))

    def test_email(self):
        self.assertTrue(type(self.instance), User)
        self.assertTrue(hasattr(self.instance, "email"))
        self.assertTrue(User.email == "")

        # check for email attribute after saving
        self.instance.save()
        all_objs = storage.all()
        key = "User." + str(self.instance.id)
        instance_obj = all_objs[key]
        self.assertTrue(key in all_objs.keys())
        self.assertTrue(hasattr(instance_obj, "email"))
        storage.delete(key)

    def test_password(self):
        self.assertTrue(type(self.instance), User)
        self.assertTrue(hasattr(self.instance, "password"))
        self.assertTrue(User.password == "")

        # check for email attribute after saving
        self.instance.save()
        all_objs = storage.all()
        key = "User." + str(self.instance.id)
        instance_obj = all_objs[key]
        self.assertTrue(key in all_objs.keys())
        self.assertTrue(hasattr(instance_obj, "password"))
        storage.delete(key)

    def test_first_name(self):
        self.assertTrue(User.first_name == "")
        self.assertTrue(type(self.instance), User)
        self.assertTrue(hasattr(self.instance, "first_name"))

    def test_last_name(self):
        self.assertTrue(User.last_name == "")
        self.assertTrue(type(self.instance), User)
        self.assertTrue(hasattr(self.instance, "last_name"))


if __name__ == "__main__":
    unittest.main()
