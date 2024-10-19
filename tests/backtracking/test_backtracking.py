import unittest
from py_dsa.backtracking.directions import word_search
class TestBacktracking(unittest.TestCase):
    def test1(self):
        s = word_search.Solution()
        self.assertEquals(True, s.exist(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"))
        self.assertEquals(True, s.exist(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"))
        self.assertEquals(False, s.exist(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"))



if __name__ == '__main__':
    unittest.main()