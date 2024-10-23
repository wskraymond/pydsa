import unittest
from py_dsa.dp.palindrome import longest_palindromic_subseq
class TestDP(unittest.TestCase):
    def test_is_sorted_and_rotated(self):
        s = longest_palindromic_subseq.Solution_2d_s_i()
        self.assertEquals(4, s.longestPalindromeSubseq("bbbab"))


if __name__ == '__main__':
    unittest.main()