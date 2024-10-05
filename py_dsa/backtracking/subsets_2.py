from collections import defaultdict
from typing import List,Set
class Solution_dfs_map_count:
    '''
    Given an integer array nums that may contain duplicates, return all possible subsets
    (the power set).

    The solution set must not contain duplicate subsets. Return the solution in any order.
    '''
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        if nums is None:
            return []
        
        #dict: word:count
        dict_count = defaultdict(lambda:0)
        for num in nums:
            dict_count[num]+=1
        
        unique = list(dict_count.keys())
        n = len(unique)
        res = []
        def dfs(i:int, subset:List[int]):
            if i==n:
                res.append(subset[::]) #be careful; clone a new copy
                return
            
            num = unique[i]
            if dict_count[num]>0:
                subset.append(num)
                dict_count[num]-=1

                dfs(i, subset)
                dict_count[num]+=1
                subset.pop()

            dfs(i+1, subset)
        dfs(0, [])
        return res

class Solution_dfs_sort:
    '''
    Given an integer array nums that may contain duplicates, return all possible subsets
    (the power set).

    The solution set must not contain duplicate subsets. Return the solution in any order.
    '''
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        if nums is None:
            return []
        
        n = len(nums)
        nums.sort()
        res = []
        def dfs(i:int, subset:List) -> None:
            if i==n:
                res.append(subset[::])
                return
            
            # take the number at index i
            subset.append(nums[i])
            dfs(i+1, subset)
            subset.pop()

            # skip same value of numbers and jump to next unique number
            while i+1 < n and nums[i]==nums[i+1]:
                i+=1
            dfs(i+1, subset)
        
        dfs(0,[])
        return res
