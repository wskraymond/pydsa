from typing import List
class Solution:
    '''
        nodes labeled from 0 to n - 1, find all possible paths from node 0 to node n - 1 and return them in any order.
    '''
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        '''
            graph[i] is a list of all nodes you can visit from node 
        '''

        n = len(graph)
        src,dst = 0, n-1
        res = []
        def backtrack(i:int, path:List)->None:
            if i==dst:
                res.append(path[::])
                return 
            
            for j in graph[i]:
                path.append(j)
                backtrack(j, path)
                path.pop()
        backtrack(src,[src])
        return res