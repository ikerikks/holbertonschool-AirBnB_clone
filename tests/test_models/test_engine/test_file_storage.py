#!/usr/bin/python3
"Unit tests for FileStorage class"
import unittest
from models.engine.file_storage import FileStorage
import os
from models.base_model import BaseModel
from models import storage


class TestFileStorage(unittest.TestCase):
    "Unit tests suite for FileStorage class"
    my_model = BaseModel()

    def test_instanciates(self):
        "Tests that FileStorage correctly instanciates"
        storage = FileStorage()
        self.assertIsInstance(storage, FileStorage)

    def test_file_path(self):
        """Test __file path is exited"""
        path = FileStorage._FileStorage__file_path
        self.assertEqual(str, type(path))

    def test_object(self):
        """Test __object is type dict after deserialization object - dict"""
        object_dict = FileStorage._FileStorage__objects
        self.assertEqual(dict, type(object_dict))

    def test_all(self):
        """Test FileStorage: all()"""
        """file is not exit"""
        dict_return = {}
        FileStorage.all(None)
        self.assertEqual(os.path.isfile('file.json'), True)

    def testreload(self):
        """test if reload """
        self.my_model.save()
        self.assertEqual(os.path.exists(storage._FileStorage__file_path), True)
        dobj = storage.all()
        FileStorage._FileStorage__objects = {}
        self.assertNotEqual(dobj, FileStorage._FileStorage__objects)
        storage.reload()
        for key, value in storage.all().items():
            self.assertEqual(dobj[key].to_dict(), value.to_dict())

    def testStoreBaseModel(self):
        """ Test save and reload functions """
        self.my_model.full_name = "BaseModel Instance"
        self.my_model.save()
        bm_dict = self.my_model.to_dict()
        all_objs = storage.all()


if __name__ == "__main__":
    unittest.main()
