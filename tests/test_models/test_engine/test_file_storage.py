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
        # Create and save some test objects
        base_model = BaseModel()
        user = User()
        self.storage.new(base_model)
        self.storage.new(user)
        self.storage.save()

        # Clear the objects dictionary
        FileStorage._FileStorage__objects = {}
        self.storage.reload()

        # Check if objects were reloaded correctly
        objects = self.storage.all()
        self.assertIn(f"BaseModel.{base_model.id}", objects)
        self.assertIn(f"User.{user.id}", objects)

        # Verify object attributes
        reloaded_base = objects[f"BaseModel.{base_model.id}"]
        self.assertEqual(reloaded_base.id, base_model.id)
        self.assertEqual(reloaded_base.to_dict()["__class__"], "BaseModel")
        # storage = FileStorage()
        # storage.reload()
        # all_objs = storage.all()
        # self.assertTrue(type(all_objs), dict)
        # self.assertTrue(len(all_objs) > 0)
        # self.assertTrue("reload" in FileStorage.__dict__)


if __name__ == "__main__":
    unittest.main()
