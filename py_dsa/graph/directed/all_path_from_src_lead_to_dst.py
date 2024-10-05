from collections import defaultdict
from typing import List
class Solution:
    '''

    Return true if and only if all roads from source lead to destination
    '''
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        '''
        *     1 <= n <= 104
        *     0 <= edges.length <= 104
        *     edges.length == 2
        *     0 <= ai, bi <= n - 1
        *     0 <= source <= n - 1
        *     0 <= destination <= n - 1
        *     The given graph may have self-loops and parallel edges.
        '''

        # determine whether or not all paths starting from source eventually, end at destination, that is:
            # At least one path exists from the source node to the destination node
                # #no. of path > 0
                    # all path from src has no cycle and if no cycle, there must be an vertex wihtoug outgoing edges 
            # If a path exists from the source node to a node with no outgoing edges, then that node is equal to destination.
                # only one vertex which has no outgoing edges, which is equal to destinatoin input
            # The number of possible paths from source to destination is a finite number.
                # no cycle
        
        #adj constructed by edges
        adj = defaultdict(list)
        for a,b in edges:
            adj[a].append(b)

        color = defaultdict(lambda : 'W' )
        def dfs(v:int)->bool:
            if ((v not in adj or not adj[v]) 
                and v!=destination):
                return False
            
            color[v]='G'
            for n in adj[v]:
                if color[n] == 'W':
                    if not dfs(n):
                        return False
                elif color[n] == 'G':
                    return False

            color[v]='B'
            return True
        return dfs(source)