from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right

class Solution:
    '''
        - A path in a binary tree is a sequence of nodes
            i) where each pair of adjacent nodes in the sequence has an edge connecting them.
                e.g parent, left, rigth -> it is invalid, becos there is no edge connecting left and right
            ii) A node can only appear in the sequence at most once.
                e.g we cannot re-visit the same node
        Note that the path does not need to pass through the root.
    '''
    def maxPathSum(self, root:Optional[TreeNode]) -> int:
        '''
            1. global Max: max(max, val, val + left, val + right , val + left + right )
            2. return val of dfs: max(val, val + left, val + right)
        '''
        result = root.val
        def dfs(node:Optional[TreeNode]) -> int:
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            val = node.val
            nonlocal result
            result = max([result, val, val+left, val+right, val+left+right])
            return max([val, val+left, val+right])
        dfs(root)
        return result



