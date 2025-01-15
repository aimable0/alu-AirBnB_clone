import sys
import os
import unittest
import datetime

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from base_model import BaseModel


class TestBaseModel(unittest.TestCase):

    def setUp(self):
        self.sample_base = BaseModel()

    def test_to_dict(self):
        # testing to_dict
        instance_dict = self.sample_base.to_dict()
        self.assertEqual(type(instance_dict), dict)
        self.assertIn("__class__", instance_dict)

        # testing difference between:
        # created_at of dict returned by to_dict and basemodelclass _dict_
        self.assertIs(type(instance_dict["created_at"]), str)
        self.assertIs(type(self.sample_base.__dict__["created_at"]), datetime.datetime)
        self.assertIs(type(instance_dict["updated_at"]), str)
        self.assertIs(type(self.sample_base.__dict__["updated_at"]), datetime.datetime)


if __name__ == "__main__":
    unittest.main()
