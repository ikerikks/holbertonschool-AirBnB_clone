#!/usr/bin/python3 
import unittest
from models.base_model import BaseModel
from models.amenity import Amenity
class TestAmenity(unittest.TestCase):
    """ unit tests for amenity"""
    def test_instance(self):
        "Test instance"
        hello = Amenity()
        self.assertIsInstance(hello, Amenity)

    def test_state_name(self):
        "Test state name"
        hello = Amenity()
        self.assertEqual("", hello.name)

    def test_id(self):
        "Test id"
        hello = Amenity()
        self.assertEqual(str, type(hello.id))

if __name__ == '__main__':
    unittest.main()
    