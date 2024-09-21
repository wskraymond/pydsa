import unittest
from py_dsa.in_place_op.rotate_array import BruteForce, ReverseArray_tmp2, RotateArray2

class TestInPlaceOp(unittest.TestCase):
    def test1(self):
        s = BruteForce()
        nums = [1,2,3,4,5,6,7]
        k = 3
        s.rotate(nums, k)
        self.assertEqual([5,6,7,1,2,3,4], nums)  # add assertion here
    
    def test2(self):
        s = ReverseArray_tmp2()
        nums = [1,2,3,4,5,6,7]
        k = 3
        s.rotate(nums, k)
        self.assertEqual([5,6,7,1,2,3,4], nums)  # add assertion here

    def test3(self):
        s = RotateArray2()
        nums = [1,2,3,4,5,6,7]
        k = 3
        s.rotate(nums, k)
        self.assertEqual([5,6,7,1,2,3,4], nums)  # add assertion here


if __name__ == '__main__':
    unittest.main()