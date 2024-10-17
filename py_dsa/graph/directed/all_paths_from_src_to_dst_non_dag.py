from typing import List,Set
class Solution:
    '''
        nodes labeled from 0 to n - 1, find all possible paths from node 0 to node n - 1 and return them in any order.
    '''
    def allPathsSourceTarget(self, src:int,dst:int, graph: List[List[int]]) -> List[List[int]]:
        '''
            graph[i] is a list of all nodes you can visit from node
            Non-DAG: 
                1. only visit every node once
                2. only visit destination and source once
                3. so even destination node has outgoing edge, we won't travsere...(but return)
        '''
        n = len(graph)
        res = []
        def backtrack(i:int, visit:Set[int], path:List[int]) -> None:
            if i==dst:
                res.append(path[::])
                return
            
            visit.add(i)
            for j in graph[i]:
                if j in visit:
                    continue
                path.append(j)
                backtrack(j,visit, path)
                path.pop()
            visit.remove(i)
        backtrack(src, set(), [src])
        return res