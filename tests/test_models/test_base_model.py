#!/usr/bin/python3

import unittest
from unittest import mock
from datetime import datetime
import sys
import os
import models

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))
from models.base_model import BaseModel

# from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):

    def setUp(self):
        self.sample_base = BaseModel()

    def tearDown(self): ...

    @mock.patch("models.storage")
    def test_save(self, mock_storage):
        # testing if save is appropriately updating time..
        time_1 = self.sample_base.created_at
        self.sample_base.save()
        time_2 = self.sample_base.updated_at
        self.assertIsNot(time_1, time_2)

        # another test
        self.sample_base.save()
        time_3 = self.sample_base.updated_at
        self.assertIsNot(time_2, time_3)

        # assert new and save was called
        self.assertTrue(mock_storage.new.called)
        self.assertTrue(mock_storage.save.called)

    def test_to_dict(self):
        # testing to_dict
        instance_dict = self.sample_base.to_dict()
        self.assertEqual(type(instance_dict), dict)
        self.assertIn("__class__", instance_dict)

        # testing difference between:
        # created_at of dict returned by to_dict and basemodelclass _dict_
        self.assertIs(type(instance_dict["created_at"]), str)
        self.assertIs(type(self.sample_base.__dict__["created_at"]), datetime)

        # testing difference between:
        # updated_at of dict returned by to_dict() and basemodelclass _dict_
        self.assertIs(type(instance_dict["updated_at"]), str)
        self.assertIs(type(self.sample_base.__dict__["updated_at"]), datetime)

    def test__str__(self):
        # check if the string is returned using __str__ method
        self.assertEqual(type(self.sample_base.__str__()), str)

        # check if the name of the class is in the returned string.
        self.assertIn("BaseModel", self.sample_base.__str__())

        # check if id is returned in the string
        self.assertIn(self.sample_base.id, self.sample_base.__str__())

        # check if __dict__ attributes in string returned by __str__
        self.assertIn(str(self.sample_base.__dict__), self.sample_base.__str__())


if __name__ == "__main__":
    unittest.main()
