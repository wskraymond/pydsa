import unittest
from py_dsa.graph.directed import all_path_from_src_lead_to_dst
class TestDirected(unittest.TestCase):
    def test1(self):
        s = all_path_from_src_lead_to_dst.Solution()
        # n = 3, edges = [[0,1],[0,2]], source = 0, destination = 2
        self.assertEquals(False, s.leadsToDestination(n = 3, edges = [[0,1],[0,2]], source = 0, destination = 2))
        self.assertEquals(False, s.leadsToDestination(n = 4, edges = [[0,1],[0,3],[1,2],[2,1]], source = 0, destination = 3))
        self.assertEquals(True, s.leadsToDestination(n = 4, edges = [[0,1],[0,2],[1,3],[2,3]], source = 0, destination = 3))
        self.assertEquals(False, s.leadsToDestination(n = 4, edges = [[0,1],[1,2],[2,0]], source = 0, destination = 3))


if __name__ == '__main__':
    unittest.main()