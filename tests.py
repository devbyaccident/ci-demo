import unittest
from app import add 

class TestDemo(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1,1), 2)

if __name__ == '__main__':
    unittest.main()