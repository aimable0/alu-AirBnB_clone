import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


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
        for value in self.storage.all().values():
            self.assertIsInstance(value, BaseModel)

    def test_all(self):
        obj = self.storage.all()
        self.assertTrue(type(obj) is dict)

    def test_new(self): ...

    def test_save(self): ...

    def test_reload(self): ...


if __name__ == "__main__":
    unittest.main()
