from typing import List, Set
class Solution:
    '''
    Given an m x n grid of characters board and a string word, return true if word exists in the grid.
    The same letter cell may not be used more than once.
    '''
    def exist(self, board: List[List[str]], word: str) -> bool:
        # Follow up: Could you use search pruning to make your solution faster with a larger board ?
        if not word:
            return True
        
        if not board or not board[0]:
            return False
            

        n, m,l = len(board), len(board[0]), len(word)
        def backtrack(i:int,j:int, k:int, visit:Set[int]) -> bool:
            if k == l-1: # base case
                return True
            
            #bactrack
            res = False
            for nextR,nextC in [(i+1, j), (i-1,j), (i,j+1), (i,j-1)]:
                if 0 <= nextR < n and 0 <= nextC < m: #boundary
                    if (nextR,nextC) in visit: #isValid
                        continue
                    
                    if board[nextR][nextC]!=word[k+1]: #pruning
                        continue

                    visit.add((nextR,nextC))
                    res = backtrack(nextR, nextC, k+1, visit)
                    visit.remove((nextR,nextC))
                    if res:
                        break
            return res

        visit = set()
        for i in range(n):
            for j in range(m):
                if board[i][j]!=word[0]:
                    continue

                visit.add((i,j))
                if backtrack(i,j,0, visit):
                    return True
                visit.remove((i,j))
        return False

