import unittest
from py_dsa.graph.undirected import word_ladder
class TestUndirected(unittest.TestCase):
    def test1(self):
        s = word_ladder.Solution_exact_graph_by_iterating_26()
        self.assertEquals(5, s.ladderLength(beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]))
        self.assertEquals(0, s.ladderLength(beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]))
    
    def test2(self):
        s = word_ladder.Solution_wildcard_mapping()
        self.assertEquals(5, s.ladderLength(beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]))
        self.assertEquals(0, s.ladderLength(beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]))


if __name__ == '__main__':
    unittest.main()