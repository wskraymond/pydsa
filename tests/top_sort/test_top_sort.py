import unittest
from py_dsa.top_sort import alien_dictionary
class TestTopSort(unittest.TestCase):
    def test1(self):
        s = alien_dictionary.Solution_dfs_default_dict()
        self.assertEqual("wertf", s.alienOrder(["wrt",
                "wrf",
                "er",
                "ett",
                "rftt"]))
        self.assertEqual("hernf", s.alienOrder(["hrn","hrf","er","enn","rfnn"]))
        self.assertEqual("zx", s.alienOrder(["z","x"]))
        self.assertEqual("", s.alienOrder(["z","x", "z"]))
        self.assertEqual("", s.alienOrder(["apple", "app"]))
    
    def test2(self):
        s = alien_dictionary.Solution_dfs()
        self.assertEqual("wertf", s.alienOrder(["wrt",
                "wrf",
                "er",
                "ett",
                "rftt"]))
        self.assertEqual("hernf", s.alienOrder(["hrn","hrf","er","enn","rfnn"]))
        self.assertEqual("zx", s.alienOrder(["z","x"]))
        self.assertEqual("", s.alienOrder(["z","x", "z"]))
        self.assertEqual("", s.alienOrder(["apple", "app"]))
    
    def test3(self):
        s = alien_dictionary.Solution_bfs()
        self.assertEqual("wertf", s.alienOrder(["wrt",
                "wrf",
                "er",
                "ett",
                "rftt"]))
        self.assertEqual("hernf", s.alienOrder(["hrn","hrf","er","enn","rfnn"]))
        self.assertEqual("zx", s.alienOrder(["z","x"]))
        self.assertEqual("", s.alienOrder(["z","x", "z"]))
        self.assertEqual("", s.alienOrder(["apple", "app"]))


if __name__ == '__main__':
    unittest.main()