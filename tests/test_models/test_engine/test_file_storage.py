import unittest
from models.engine.file_storage import FileStorage
import os


class TestFileStorage(unittest.TestCase):
    """A unit test class to test thouroughly the class FileStorage

    Args:
        unittest (class): test class that provides me with test functions.
    """

    def setUp(self):
        """an instance of storage to run tests on"""
        self.storage = FileStorage()

    def test_file_path(self):
        """test if the file_path is valid or not"""
        # test for valid file.extension
        os.path.isfile("alu-AirBnB_clone\file.json")
        # valid file_path
        os.path.exists("alu-AirBnB_clone\file.json")
