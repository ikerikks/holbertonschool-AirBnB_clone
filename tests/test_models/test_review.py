"Unit tests for Review class"
import unittest
from models.review import Review
from models.user import User
from models.place import Place

class TestReview(unittest.TestCase):
    "Unit tests suite for Review class"

    def test_place_id(self):
        "Test place id"
        hello = Review()
        self.assertEqual("", hello.place_id)

    def test_user_id(self):
        "Test user id"
        hello = Review()
        self.assertEqual("", hello.user_id)

    def test_text(self):
        "Test text"
        hello = Review()
        self.assertEqual("", hello.text)

    def test_instance(self):
        "Test instance"
        hello = Review()
        self.assertIsInstance(hello, Review)
    
if __name__ == '__main__':
    unittest.main()