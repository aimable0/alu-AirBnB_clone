import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import json


class TestFileStorage(unittest.TestCase):
    """A unit test class to test thouroughly the class FileStorage

    Args:
        unittest (class): test class that provides me with test functions.
    """

    def setUp(self):
        """an instance of storage to run tests on"""
        self.new_model = BaseModel()
        self.new_model.name = "Sample_Model"
        self.new_model.my_number = 23
        self.new_model.save()
        self.storage = FileStorage()
        self.storage.reload()

    def test__file_path(self):
        """test if the file_path is valid or not"""
        # test whether _file_path is private
        try:
            with self.assertRaises(AttributeError):
                file_path = self.storage.__file_path
        except:
            raise Exception("Trying to assign file name didn't raise Attribute Error")

    def test__objects(self):
        """Test if objects contains base model instances."""
        for value in self.storage.all().values():
            self.assertIsInstance(value, BaseModel)

    def test_all(self):
        """Test that all returns the FileStorage.__objects attr"""
        storage = FileStorage()
        new_dict = storage.all()
        self.assertTrue(type(new_dict) is dict)
        self.assertIs(new_dict, storage._FileStorage__objects)

    def test_new(self):
        """test that new adds an object to the FileStorage.__objects attr"""
        storage = FileStorage()
        instance = BaseModel()
        storage.new(instance)
        self.assertIn(instance, (storage._FileStorage__objects).values())

    def test_save(self):
        """Test that save properly saves objects to file.json"""
        storage = FileStorage()
        instance = BaseModel()
        storage.new(instance)
        storage.save()
        with open("file.json", "r") as file:
            objs = json.load(file)
            self.assertIn(instance.to_dict(), objs.values())

    def test_reload(self):
        storage = FileStorage()
        storage.reload()
        all_objs = storage.all()
        self.assertTrue(type(all_objs), dict)
        self.assertTrue(len(all_objs) > 0)

if __name__ == "__main__":
    unittest.main()
