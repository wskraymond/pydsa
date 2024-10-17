from typing import List
class Solution_iterative:
    '''
        Given an integer array nums of unique elements, return all possible 
        subsets (the power set).
    '''
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if nums is None:
            return []
        
        res, n = [], len(nums)
        def backtrack(start:int,subset:List[int]) -> None:
            res.append(subset[::])

            for i in range(start, n):
                subset.append(nums[i])
                backtrack(i+1, subset)
                subset.pop()
        backtrack(0,[])
        return res

class Solution_dfs:
    '''
        Given an integer array nums of unique elements, return all possible 
        subsets (the power set).
    '''
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if nums is None:
            return []
        
        res, n = [], len(nums)
        def dfs(i:int, subset:List[int]) -> None:
            if i==n:
                res.append(subset[::])
                return 
            
            subset.append(nums[i])
            dfs(i+1, subset)
            subset.pop()

            dfs(i+1, subset)
            return
        dfs(0, [])
        return res

# https://leetcode.com/problems/subsets/solutions/5186398/faster-less-mem-3-methods-detailed-approach-recursion-bit-mani-iterative-python-java-c/
class Solution_clone:
    '''
        Given an integer array nums of unique elements, return all possible 
        subsets (the power set).
    '''
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if nums is None:
            return []
        
        res= [[]]
        for num in nums:
            res += [ s + [num] for s in res]
        return res

class Solution_bitset:
    '''
        Given an integer array nums of unique elements, return all possible 
        subsets (the power set).
    '''
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if nums is None:
            return []
        
        #iterate bitset
        #add all corresponding 'one' in a bitset
        #index for bit sequence: n-1......0
        n = len(nums)
        res = []
        for bitset in range(1<<n):
            subset = []
            for j in range(n):
                if bitset & (1<<j) != 0:
                    subset.append(nums[j])
            res.append(subset)
        return res