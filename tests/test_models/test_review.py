#!/usr/bin/python3

import unittest
from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    """test class: Review"""

    def setUp(self):
        """create an instance before test_... is run"""
        self.instance = Review()

    def test_Review(self):
        """test if Review inherits from BaseModel"""
        self.assertTrue(issubclass(Review, BaseModel))
        self.assertIsInstance(self.instance, BaseModel)
        self.assertTrue(hasattr(self.instance, "id"))
        self.assertTrue(hasattr(self.instance, "created_at"))
        self.assertTrue(hasattr(self.instance, "updated_at"))

    def test_place_id(self):
        """test if place_id is an attribute of Review"""
        self.assertTrue(type(self.instance), Review)
        self.assertTrue(hasattr(self.instance, "place_id"))
        self.assertTrue(Review.place_id == "")

    def test_user_id(self):
        """test if user_id is an attribute of Review"""
        self.assertTrue(type(self.instance), Review)
        self.assertTrue(hasattr(self.instance, "user_id"))
        self.assertTrue(Review.user_id == "")

    def test_text(self):
        """test if user_id is an attribute of Review"""
        self.assertTrue(type(self.instance), Review)
        self.assertTrue(hasattr(self.instance, "text"))
        self.assertTrue(Review.text == "")


if __name__ == "__main__":
    unittest.main()
