import unittest
from py_dsa.sliding_window import longest_substr_at_most_k_distinct
class TestPrefixSum(unittest.TestCase):
    def test_longest_substr_at_most_k_distinct(self):
        s = longest_substr_at_most_k_distinct.Solution_dict()
        self.assertEquals(10, s.lengthOfLongestSubstringKDistinct("12222333444556677", 3))
        self.assertEquals(3, s.lengthOfLongestSubstringKDistinct(s = "eceba", k = 2))
        self.assertEquals(2, s.lengthOfLongestSubstringKDistinct(s = "aa", k = 1))
        self.assertEquals(0, s.lengthOfLongestSubstringKDistinct(s = "aa", k = 0))
        self.assertEquals(0, s.lengthOfLongestSubstringKDistinct(s = "", k = 1))

    def test_longest_substr_at_most_k_distinct_2(self):
        s = longest_substr_at_most_k_distinct.Solution_counter()
        self.assertEquals(10, s.lengthOfLongestSubstringKDistinct("12222333444556677", 3))
        self.assertEquals(3, s.lengthOfLongestSubstringKDistinct(s = "eceba", k = 2))
        self.assertEquals(2, s.lengthOfLongestSubstringKDistinct(s = "aa", k = 1))
        self.assertEquals(0, s.lengthOfLongestSubstringKDistinct(s = "aa", k = 0))
        self.assertEquals(0, s.lengthOfLongestSubstringKDistinct(s = "", k = 1))
    
    def test_longest_substr_at_most_k_distinct_3(self):
        s = longest_substr_at_most_k_distinct.Solution_defaultdict()
        self.assertEquals(10, s.lengthOfLongestSubstringKDistinct("12222333444556677", 3))
        self.assertEquals(3, s.lengthOfLongestSubstringKDistinct(s = "eceba", k = 2))
        self.assertEquals(2, s.lengthOfLongestSubstringKDistinct(s = "aa", k = 1))
        self.assertEquals(0, s.lengthOfLongestSubstringKDistinct(s = "aa", k = 0))
        self.assertEquals(0, s.lengthOfLongestSubstringKDistinct(s = "", k = 1))
        


if __name__ == '__main__':
    unittest.main()