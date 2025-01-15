import sys
import os
import unittest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from base_model import BaseModel

class TestBaseModel(unittest.TestCase):

    def setUp(self):
        self.sample_base = BaseModel()

    def tearDown(self):
        ...

    def test_save(self):
        # testing if save is appropriately updating time..
        time_1 = self.sample_base.created_at
        self.sample_base.save()
        time_2 = self.sample_base.updated_at
        self.assertIsNot(time_1, time_2)

        # another test
        self.sample_base.save()
        time_3 = self.sample_base.updated_at
        self.assertIs(time_2, time_3)


if __name__ == "__main__":
    unittest.main()