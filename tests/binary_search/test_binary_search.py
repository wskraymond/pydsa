import unittest
from py_dsa.binary_search import sqrt
class TestBinarySearch(unittest.TestCase):
    def test_sqrt(self):
        s = sqrt.Solution()
        self.assertEqual(2, s.mySqrt(4))
        self.assertEqual(2, s.mySqrt(8))
        self.assertEqual(3, s.mySqrt(9))


if __name__ == '__main__':
    unittest.main()