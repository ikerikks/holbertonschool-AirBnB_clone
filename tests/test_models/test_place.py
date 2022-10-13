#!/usr/bin/python3
"""Unittest module for Place"""
import unittest
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.city import City



class TestPlace(unittest.TestCase):
    """class testing the Place class"""

    def test_instance(self):
        """test the creation of a Place instance"""
        p = Place()
        self.assertTrue(hasattr(p, 'city_id'))
        self.assertTrue(hasattr(p, 'user_id'))
        self.assertTrue(hasattr(p, 'name'))
        self.assertTrue(hasattr(p, 'description'))
        self.assertTrue(hasattr(p, 'number_rooms'))
        self.assertTrue(hasattr(p, 'number_bathrooms'))
        self.assertTrue(hasattr(p, 'max_guest'))
        self.assertTrue(hasattr(p, 'price_by_night'))
        self.assertTrue(hasattr(p, 'latitude'))
        self.assertTrue(hasattr(p, 'longitude'))
        self.assertTrue(hasattr(p, 'amenity_ids'))
        self.assertTrue(type(p.city_id), str)
        self.assertTrue(type(p.user_id), str)
        self.assertTrue(type(p.name), str)
        self.assertTrue(type(p.description), str)
        self.assertTrue(type(p.number_rooms), int)
        self.assertTrue(type(p.number_bathrooms), int)
        self.assertTrue(type(p.max_guest), int)
        self.assertTrue(type(p.price_by_night), int)
        self.assertTrue(type(p.latitude), float)
        self.assertTrue(type(p.longitude), float)
        self.assertTrue(type(p.amenity_ids), list)
        self.assertEqual(p.city_id, '')
        self.assertEqual(p.user_id, '')
        self.assertEqual(p.name, '')
        self.assertEqual(p.description, '')
        self.assertEqual(p.number_rooms, 0)
        self.assertEqual(p.number_bathrooms, 0)
        self.assertEqual(p.max_guest, 0)
        self.assertEqual(p.price_by_night, 0)
        self.assertEqual(p.latitude, 0.0)
        self.assertEqual(p.longitude, 0.0)
        self.assertEqual(p.amenity_ids, [])
        self.assertEqual(len(p.amenity_ids), 0)
        b = City()
        p.city_id = b.id
        self.assertEqual(p.city_id, b.id)
        c = User()
        p.user_id = c.id
        self.assertEqual(p.user_id, c.id)
        p.name = 'Gabriel'
        self.assertEqual(p.name, 'Gabriel')
        p.description = 'Description'
        self.assertEqual(p.description, 'Description')
        p.number_rooms = 5
        self.assertEqual(p.number_rooms, 5)
        p.number_bathrooms = 2
        self.assertEqual(p.number_bathrooms, 2)
        p.max_guest = 8
        self.assertEqual(p.max_guest, 8)
        p.price_by_night = 30
        self.assertEqual(p.price_by_night, 30)
        p.latitude = 48.07
        self.assertEqual(p.latitude, 48.07)
        p.longitude = -0.76
        self.assertEqual(p.longitude, -0.76)
        
    def test_str(self):
        """Test the string output of the class"""
        p = Place()
        self.assertEqual(str(p), f"[Place] ({p.id}) {p.__dict__}")


if __name__ == '__main__':
    unittest.main()
