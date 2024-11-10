import unittest
from py_dsa.two_pointers import three_sum_smaller
class TestTwoPointers(unittest.TestCase):
    def test1(self):
        s = three_sum_smaller.Solution()
        self.assertEqual(2, s.threeSumSmaller(nums = [-2,0,1,3], target = 2))
        self.assertEqual(0, s.threeSumSmaller(nums = [], target = 0))
        self.assertEqual(0, s.threeSumSmaller(nums = [0], target = 0))

    def test2(self):
        s = three_sum_smaller.Solution_bruteforce()
        self.assertEqual(2, s.threeSumSmaller(nums = [-2,0,1,3], target = 2))
        self.assertEqual(0, s.threeSumSmaller(nums = [], target = 0))
        self.assertEqual(0, s.threeSumSmaller(nums = [0], target = 0))

if __name__ == '__main__':
    unittest.main()