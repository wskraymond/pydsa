import unittest
from py_dsa.prefix_sum import continuous_subarr_sum, subarray_sum_equals_k
class TestPrefixSum(unittest.TestCase):
    def test_prefix_sum_1(self):
        s = continuous_subarr_sum.Solution_bruteforce()
        self.assertEqual(True, s.checkSubarraySum(nums=[23,2,6,4,7], k=6))
        self.assertEqual(True, s.checkSubarraySum(nums=[1,1,1,1,1,1], k=6))
        self.assertEqual(True, s.checkSubarraySum(nums=[0,0], k=3))
        self.assertEqual(False, s.checkSubarraySum(nums=[0], k=3))
        self.assertEqual(False, s.checkSubarraySum(nums=[23,2,6,4,7], k=13))
        self.assertEqual(True, s.checkSubarraySum(nums=[23,2,4,6,7], k=6))
    
    def test_prefix_sum_2(self):
        s = subarray_sum_equals_k.Solution_bruteforce()
        self.assertEqual(2, s.subarraySum(nums=[1,1,1], k=2))
        self.assertEqual(2, s.subarraySum(nums=[1,2,3], k=3))
        self.assertEqual(0, s.subarraySum(nums=[1], k=0))


if __name__ == '__main__':
    unittest.main()