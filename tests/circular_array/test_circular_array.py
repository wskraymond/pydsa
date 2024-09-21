import unittest
from py_dsa.circular_array import is_sorted_and_rotated
class TestCircularArray(unittest.TestCase):
    def test_is_sorted_and_rotated(self):
        s = is_sorted_and_rotated.Solution()
        self.assertTrue(s.check([1,2,3,4,5]))
        self.assertTrue(s.check([]))
        self.assertTrue(s.check([4,5,1,2,3]))
        self.assertFalse(s.check([4,5,1,6,3]))
        self.assertTrue(s.check([1,1,1,2,2,3]))
        self.assertTrue(s.check([2,2,3,3,1,1,1]))
        self.assertTrue(s.check([1,1,1]))
        self.assertTrue(s.check([1,0,1,1]))


if __name__ == '__main__':
    unittest.main()