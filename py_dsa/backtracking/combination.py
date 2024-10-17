from typing import List
class Solution:
    '''
        Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].
    '''
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def backtrack(start:int, c:List[int]) -> None:
            if len(c)==k:
                res.append(c[::])
                return
            
            for i in range(start, n):
                c.append(i+1)
                backtrack(i+1, c)
                c.pop()
        backtrack(0, [])
        return res