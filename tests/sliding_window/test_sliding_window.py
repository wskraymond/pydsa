import unittest
from py_dsa.sliding_window import longest_substr_at_most_k_distinct
class TestPrefixSum(unittest.TestCase):
    def test_longest_substr_at_most_k_distinct(self):
        s = longest_substr_at_most_k_distinct.Solution_dict()
        self.assertEqual(10, s.lengthOfLongestSubstringKDistinct("12222333444556677", 3))
        self.assertEqual(3, s.lengthOfLongestSubstringKDistinct(s = "eceba", k = 2))
        self.assertEqual(2, s.lengthOfLongestSubstringKDistinct(s = "aa", k = 1))
        self.assertEqual(0, s.lengthOfLongestSubstringKDistinct(s = "aa", k = 0))
        self.assertEqual(0, s.lengthOfLongestSubstringKDistinct(s = "", k = 1))

    def test_longest_substr_at_most_k_distinct_2(self):
        s = longest_substr_at_most_k_distinct.Solution_counter()
        self.assertEqual(10, s.lengthOfLongestSubstringKDistinct("12222333444556677", 3))
        self.assertEqual(3, s.lengthOfLongestSubstringKDistinct(s = "eceba", k = 2))
        self.assertEqual(2, s.lengthOfLongestSubstringKDistinct(s = "aa", k = 1))
        self.assertEqual(0, s.lengthOfLongestSubstringKDistinct(s = "aa", k = 0))
        self.assertEqual(0, s.lengthOfLongestSubstringKDistinct(s = "", k = 1))
    
    def test_longest_substr_at_most_k_distinct_3(self):
        s = longest_substr_at_most_k_distinct.Solution_defaultdict()
        self.assertEqual(10, s.lengthOfLongestSubstringKDistinct("12222333444556677", 3))
        self.assertEqual(3, s.lengthOfLongestSubstringKDistinct(s = "eceba", k = 2))
        self.assertEqual(2, s.lengthOfLongestSubstringKDistinct(s = "aa", k = 1))
        self.assertEqual(0, s.lengthOfLongestSubstringKDistinct(s = "aa", k = 0))
        self.assertEqual(0, s.lengthOfLongestSubstringKDistinct(s = "", k = 1))
        


if __name__ == '__main__':
    unittest.main()