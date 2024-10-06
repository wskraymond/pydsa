# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


from typing import Optional

'''
The single quotes around 'Node' in Optional['Node'] are used to handle forward references. This is necessary when the class Node is not yet fully defined at the point where it is referenced in the type hint. By using single quotes, you tell the type checker to treat 'Node' as a string that will be resolved to the actual Node class later.

Here’s why this is important:

Forward Reference: When you define a class, you might want to reference the class itself within its own definition or in methods that are defined before the class is fully defined. Using single quotes allows you to do this without causing a NameError.
Type Checking: The type checker can still understand and validate the type hints correctly even if the class is not yet defined.
'''
class Solution:
    '''
        Given a reference of a node in a connected undirected graph.
        Return a deep copy (clone) of the graph.
    '''
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        '''
        Constraints:
            The number of nodes in the graph is in the range [0, 100].
            1 <= Node.val <= 100
            Node.val is unique for each node.
            There are no repeated edges and no self-loops in the graph.
            The Graph is connected and all nodes can be visited starting from the given node.
        '''
        if node is None:
            return None
        #pre-order dfs: traverse the old graph to create every cloned node if it's not visited yet
        #map: old -> new if already visited, we need to link up the created node with the currently travsersing node.
        old_to_new = {}
        def dfs(node:Node) -> Node:
            if node in old_to_new:
                return old_to_new[node]
            new_node = Node(node.val)
            old_to_new[node] = new_node
            for neighbour in node.neighbors:
                new_neighbour = dfs(neighbour)
                new_node.neighbors.append(new_neighbour)
            return new_node
        return dfs(node)