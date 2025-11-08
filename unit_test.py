import unittest
from math_operations import add , subtract

class TestMathOperations(unittest.TestCase):

    def test_add(self):
        # Normal cases
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)
        # Edge cases
        self.assertEqual(add(-1e10, 1e10), 0)
        self.assertEqual(add(1.5, 2.5), 4.0)
        # Invalid inputs
        with self.assertRaises(ValueError):
            add("a", 1)
        with self.assertRaises(ValueError):
            add(1, None)

    def test_subtract(self):
        # Normal cases
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(-1, -1), 0)
        self.assertEqual(subtract(0, 0), 0)
        # Edge cases
        self.assertEqual(subtract(-1e10, 1e10), -2e10)
        self.assertEqual(subtract(2.5, 1.5), 1.0)
        # Invalid inputs
        with self.assertRaises(ValueError):
            subtract("a", 1)
        with self.assertRaises(ValueError):
            subtract(1, None)

if __name__ == '__main__':
    unittest.main()
