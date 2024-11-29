import unittest
from py_dsa.heap import high_five
class TestHeap(unittest.TestCase):
    def test_highfive(self):
        s = high_five.Solution()
        self.assertEqual([[1,87],[2,88]], s.highFive([[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]))
        self.assertEqual([[1,100],[7,100]], s.highFive([[1,100],[7,100],[1,100],[7,100],[1,100],[7,100],[1,100],[7,100],[1,100],[7,100]]))
    
    def test_highfive2(self):
        s = high_five.Solution_pre_sort()
        self.assertEqual([[1,87],[2,88]], s.highFive([[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]))
        self.assertEqual([[1,100],[7,100]], s.highFive([[1,100],[7,100],[1,100],[7,100],[1,100],[7,100],[1,100],[7,100],[1,100],[7,100]]))


if __name__ == '__main__':
    unittest.main()