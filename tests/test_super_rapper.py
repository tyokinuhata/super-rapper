import unittest
from src.super_rapper.super_rapper import SuperRapper

class TestSuperRapper(unittest.TestCase):
    def test_hello_world(self):
        rapper = SuperRapper()
        message = rapper.hello_world()
        expected = "hello, world!"
        self.assertEqual(expected, message)

if __name__ == "__main__":
    unittest.main()
