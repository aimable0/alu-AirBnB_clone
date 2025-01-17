#!/usr/bin/python3

import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """test class: Amenity"""

    def setUp(self):
        """create an instance before test_... is run"""
        self.instance = Amenity()

    def test_Amenity(self):
        """test if Amenity inherits from BaseModel"""
        self.assertTrue(issubclass(Amenity, BaseModel))
        self.assertIsInstance(self.instance, BaseModel)
        self.assertTrue(hasattr(self.instance, "id"))
        self.assertTrue(hasattr(self.instance, "created_at"))
        self.assertTrue(hasattr(self.instance, "updated_at"))

    def test_name(self):
        """test if name is an attribute of Amenity"""
        self.assertTrue(type(self.instance), Amenity)
        self.assertTrue(hasattr(self.instance, "name"))
        self.assertTrue(Amenity.name == "")


if __name__ == "__main__":
    unittest.main()
