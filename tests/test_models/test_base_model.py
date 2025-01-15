import unittest
from datetime import datetime
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):

    def setUp(self):
        self.sample_base = BaseModel()

    def tearDown(self): ...

    def test_save(self):
        # testing if save is appropriately updating time..
        time_1 = self.sample_base.created_at
        self.sample_base.save()
        time_2 = self.sample_base.updated_at
        self.assertIsNot(time_1, time_2)

        # another test
        self.sample_base.save()
        time_3 = self.sample_base.updated_at
        self.assertIsNot(time_2, time_3)

    def test_to_dict(self):
        # testing to_dict
        instance_dict = self.sample_base.to_dict()
        self.assertEqual(type(instance_dict), dict)
        self.assertIn("__class__", instance_dict)

        # testing difference between:
        # created_at of dict returned by to_dict and basemodelclass _dict_
        self.assertIs(type(instance_dict["created_at"]), str)
        self.assertIs(type(self.sample_base.__dict__["created_at"]), datetime)
        self.assertIs(type(instance_dict["updated_at"]), str)
        self.assertIs(type(self.sample_base.__dict__["updated_at"]), datetime)


if __name__ == "__main__":
    unittest.main()
