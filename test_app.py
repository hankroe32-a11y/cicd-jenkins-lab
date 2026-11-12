import unittest
from app import add, subtract, is_even

class TestApp(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(10, 5), 15)
        self.assertEqual(add(-2, 2), 0)

    def test_subtract(self):
        self.assertEqual(subtract(10, 4), 6)
        self.assertEqual(subtract(0, 5), -5)

    def test_is_even(self):
        self.assertTrue(is_even(4))
        self.assertFalse(is_even(7))

if __name__ == '__main__':
    unittest.main()
