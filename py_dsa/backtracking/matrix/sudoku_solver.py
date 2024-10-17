from typing import List
'''
    Ref Solution: https://leetcode.ca/2016-01-06-37-Sudoku-Solver/ 
'''
class Solution:
    # The '.' character indicates empty cells.
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n = len(board)
        rows, cols, subs = [set()]*n, [set()]*n, [set()]*n
        sub_func = lambda i,j: i/3*3 + j/3 
        
        for i in range(n):
            for j in range(n):
                val = board[i][j]
                if val != '-':
                    rows[i].add(val)
                    cols[j].add(val)
                    subs[sub_func(i,j)].add(val)
        
        def backtrack(i, j):
            if i==n or j==n:
                return True
            
            


        