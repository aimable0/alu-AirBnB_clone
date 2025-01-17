#!/usr/bin/python3

import unittest
from models.place import Place
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):
    """test class: Place"""

    def setUp(self):
        """create an instance before test_... is run"""
        self.instance = Place()

    def test_Place(self):
        """test if Place inherits from BaseModel"""
        self.assertTrue(issubclass(Place, BaseModel))
        self.assertIsInstance(self.instance, BaseModel)
        self.assertTrue(hasattr(self.instance, "id"))
        self.assertTrue(hasattr(self.instance, "created_at"))
        self.assertTrue(hasattr(self.instance, "updated_at"))

    def test_city_id(self):
        """test if city_id is an attribute of Place"""
        self.assertTrue(type(self.instance), Place)
        self.assertTrue(hasattr(self.instance, "city_id"))
        self.assertTrue(Place.city_id == "")

    def test_user_id(self):
        """test if user_id is an attribute of Place"""
        self.assertTrue(type(self.instance), Place)
        self.assertTrue(hasattr(self.instance, "user_id"))
        self.assertTrue(Place.user_id == "")

    def test_name(self):
        """test if name is an attribute of Place"""
        self.assertTrue(type(self.instance), Place)
        self.assertTrue(hasattr(self.instance, "name"))
        self.assertTrue(Place.name == "")

    def test_description(self):
        """test if description is an attribute of Place"""
        self.assertTrue(type(self.instance), Place)
        self.assertTrue(hasattr(self.instance, "description"))
        self.assertTrue(Place.description == "")

    def test_number_rooms(self):
        """test if number_rooms is an attribute of Place"""
        self.assertTrue(type(self.instance), Place)
        self.assertTrue(hasattr(self.instance, "number_rooms"))
        self.assertTrue(Place.number_rooms == 0)

    def test_number_bathrooms(self):
        """test if number_bathrooms is an attribute of Place"""
        self.assertTrue(type(self.instance), Place)
        self.assertTrue(hasattr(self.instance, "number_bathrooms"))
        self.assertTrue(Place.number_bathrooms == 0)

    def test_max_guest(self):
        """test if max_guest is an attribute of Place"""
        self.assertTrue(type(self.instance), Place)
        self.assertTrue(hasattr(self.instance, "max_guest"))
        self.assertTrue(Place.max_guest == 0)

    def test_price_by_night(self):
        """test if price_by_night is an attribute of Place"""
        self.assertTrue(type(self.instance), Place)
        self.assertTrue(hasattr(self.instance, "price_by_night"))
        self.assertTrue(Place.price_by_night == 0)

    def test_latitude(self):
        """test if latitude is an attribute of Place"""
        self.assertTrue(type(self.instance), Place)
        self.assertTrue(hasattr(self.instance, "latitude"))
        self.assertTrue(Place.latitude == 0.0)

    def test_longitude(self):
        """test if longitude is an attribute of Place"""
        self.assertTrue(type(self.instance), Place)
        self.assertTrue(hasattr(self.instance, "longitude"))
        self.assertTrue(Place.longitude == 0.0)

    def test_amenity_ids(self):
        """test if amenity_ads is an attribute of Place"""
        self.assertTrue(type(self.instance), Place)
        self.assertTrue(hasattr(self.instance, "amenity_ids"))
        self.assertTrue(Place.amenity_ids == [])


if __name__ == "__main__":
    unittest.main()
