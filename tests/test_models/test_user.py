#!/usr/bin/python3

import unittest
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """test class: User"""

    def setUp(self):
        """create an instance before test_... is run"""
        self.instance = User()

    def test_user(self):
        """test if User inherits from BaseModel"""
        self.assertTrue(issubclass(User, BaseModel))
        self.assertIsInstance(self.instance, BaseModel)
        self.assertTrue(hasattr(self.instance, "id"))
        self.assertTrue(hasattr(self.instance, "created_at"))
        self.assertTrue(hasattr(self.instance, "updated_at"))

    def test_email(self):
        """test if email is an attribute of User"""
        self.assertTrue(type(self.instance), User)
        self.assertTrue(hasattr(self.instance, "email"))
        self.assertTrue(User.email == "")

    def test_password(self):
        """test if password is an attribute of User"""
        self.assertTrue(type(self.instance), User)
        self.assertTrue(hasattr(self.instance, "password"))
        self.assertTrue(User.password == "")

        # check for password attribute after saving
        # self.instance.save()
        # all_objs = storage.all()
        # key = "User." + str(self.instance.id)
        # instance_obj = all_objs[key]
        # self.assertTrue(key in all_objs.keys())
        # self.assertTrue(hasattr(instance_obj, "password"))
        # storage.delete(key)

    def test_first_name(self):
        """test if first_name is an attribute of User"""
        self.assertTrue(User.first_name == "")
        self.assertTrue(type(self.instance), User)
        self.assertTrue(hasattr(self.instance, "first_name"))

    def test_last_name(self):
        """test if last_name is an attribute of User"""
        self.assertTrue(User.last_name == "")
        self.assertTrue(type(self.instance), User)
        self.assertTrue(hasattr(self.instance, "last_name"))


if __name__ == "__main__":
    unittest.main()
