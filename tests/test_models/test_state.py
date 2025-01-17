#!/usr/bin/python3

import unittest
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """test class: State"""

    def setUp(self):
        """create an instance before test_... is run"""
        self.instance = State()

    def test_state(self):
        """test if State inherits from BaseModel"""
        self.assertTrue(issubclass(State, BaseModel))
        self.assertIsInstance(self.instance, BaseModel)
        self.assertTrue(hasattr(self.instance, "id"))
        self.assertTrue(hasattr(self.instance, "created_at"))
        self.assertTrue(hasattr(self.instance, "updated_at"))

    def test_name(self):
        """test if name is an attribute of State"""
        self.assertTrue(type(self.instance), State)
        self.assertTrue(hasattr(self.instance, "name"))
        self.assertTrue(State.name == "")


if __name__ == "__main__":
    unittest.main()
