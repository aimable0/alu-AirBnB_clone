#!/usr/bin/python3

import unittest
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """test class: City"""

    def setUp(self):
        """create an instance before test_... is run"""
        self.instance = City()

    def test_City(self):
        """test if City inherits from BaseModel"""
        self.assertTrue(issubclass(City, BaseModel))
        self.assertIsInstance(self.instance, BaseModel)
        self.assertTrue(hasattr(self.instance, "id"))
        self.assertTrue(hasattr(self.instance, "created_at"))
        self.assertTrue(hasattr(self.instance, "updated_at"))

    def test_name(self):
        """test if name is an attribute of City"""
        self.assertTrue(type(self.instance), City)
        self.assertTrue(hasattr(self.instance, "name"))
        self.assertTrue(City.name == "")

    def test_state_id(self):
        """test if state_id is an attribute of City"""
        self.assertTrue(type(self.instance), City)
        self.assertTrue(hasattr(self.instance, "state_id"))
        self.assertTrue(City.state_id == "")


if __name__ == "__main__":
    unittest.main()
