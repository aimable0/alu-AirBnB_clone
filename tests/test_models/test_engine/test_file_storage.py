import unittest
from models.engine.file_storage import FileStorage
import sys
import os

# # sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../")))
# from models.base_model import BaseModel

class TestFileStorage(unittest.TestCase):
    """A unit test class to test thouroughly the class FileStorage

    Args:
        unittest (class): test class that provides me with test functions.
    """

    def setUp(self):
        """an instance of storage to run tests on"""
        self.storage = FileStorage()

    def test__file_path(self):
        """test if the file_path is valid or not"""

        # test whether _file_path is private
        try:
            with self.assertRaises(AttributeError):
                file_path = self.storage.__file_path
        except:
            raise Exception("Trying to assing file name didn't raise Attribute Error")


        # valid file_path
        # self.assertTrue(os.path.exists("alu-AirBnB_clone\fiale.json"))
