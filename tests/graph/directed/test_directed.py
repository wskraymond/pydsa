import unittest
from py_dsa.graph.directed import all_path_from_src_lead_to_dst
from py_dsa.graph.directed import all_paths_from_src_to_dst_non_dag
from functools import cmp_to_key

class TestDirected(unittest.TestCase):
    def test1(self):
        s = all_path_from_src_lead_to_dst.Solution()
        # n = 3, edges = [[0,1],[0,2]], source = 0, destination = 2
        self.assertEqual(False, s.leadsToDestination(n = 3, edges = [[0,1],[0,2]], source = 0, destination = 2))
        self.assertEqual(False, s.leadsToDestination(n = 4, edges = [[0,1],[0,3],[1,2],[2,1]], source = 0, destination = 3))
        self.assertEqual(True, s.leadsToDestination(n = 4, edges = [[0,1],[0,2],[1,3],[2,3]], source = 0, destination = 3))
        self.assertEqual(False, s.leadsToDestination(n = 4, edges = [[0,1],[1,2],[2,0]], source = 0, destination = 3))
        
    def test2_1(self):
        s = all_paths_from_src_to_dst_non_dag.Solution()
        e = [[2, 1, 3], [2, 0, 1, 3], [2, 0, 3]]
        a = s.allPathsSourceTarget(2, 3, [ [1,2,3],[3],[0,1],[]])

        '''
        using the cmp_to_key function allows the sort() method to compare two lists from eArr. 
        This way, the custom comparator can be used to determine the order of the nested lists based on the rules you've defined.
        '''
        def comparator(arr1, arr2):
            min_len = min(len(arr2), len(arr2))
            for i in range(min_len):
                if arr1[i]==arr2[i]:
                    continue

                return arr1[i] - arr2[i]
            return len(arr1) - len(arr2)
        
        e.sort(key=cmp_to_key(comparator))
        a.sort(key=cmp_to_key(comparator))

        '''
            1. Python's == operator does check deep equality for nested lists
            2. unittest's assertEqual method also checks for deep equality in nested lists
        '''
        print("a=", a, " e=", e)
        self.assertEqual(a, e)
    
    def test2_2(self):
        s = all_paths_from_src_to_dst_non_dag.Solution()
        e = [[2, 1, 3], [2, 0, 1, 3], [2, 0, 3]]
        a = s.allPathsSourceTarget(2, 3, [ [1,2,3],[3],[0,1],[]])

        '''
            1. Python's == operator does check deep equality for nested lists
            2. unittest's assertEqual method also checks for deep equality in nested lists
            3. When sorted() is applied to a list of lists, it compares each sub-list element-wise in a lexicographical order (like in a dictionary)
        '''
        print("a=", sorted(a), " e=", sorted(e))
        self.assertEqual(sorted(a), sorted(e))



if __name__ == '__main__':
    unittest.main()