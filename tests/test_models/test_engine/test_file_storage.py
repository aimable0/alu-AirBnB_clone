import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
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
        # self.storage.reload()

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
        """Test successful reload of objects from file"""
        # Add an object and save it
        self.storage.new(self.new_model)
        self.storage.save()

        # Clear the __objects dictionary
        self.storage._FileStorage__objects = {}

        # Reload the objects from the file
        self.storage.reload()

        # Assert that the object is back in __objects
        key = f"BaseModel.{self.new_model.id}"
        self.assertIn(key, self.storage.all())
        self.assertEqual(self.new_model.id, self.storage.all()[key].id)

if __name__ == "__main__":
    unittest.main()
