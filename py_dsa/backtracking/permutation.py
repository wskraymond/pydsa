from typing import List,Set
class Solution_wrong_using_unordered_set:
    '''
    Given an array nums of distinct integers, return all the possible permutations
    You can return the answer in any order.
    '''
    def permute(self, nums: List[int]) -> List[List[int]]:
        res,n = [], len(nums)
        def backtrack(visit:Set[int])->None:
            if len(visit)==n:
                res.append(list(visit)) # we have to maintain the order ......wrong!!
                return 
            
            for i in range(n):
                num = nums[i]
                if num not in visit:
                    visit.add(num)
                    backtrack(visit)
                    visit.remove(num)

        backtrack(set()) 
        return res #n!

class Solution_ordered:
    '''
    Given an array nums of distinct integers, return all the possible permutations
    You can return the answer in any order.
    '''
    def permute(self, nums: List[int]) -> List[List[int]]:
        res,n = [], len(nums)
        # no built-in orderedSet but OrderedDict
        def backtrack(p:List[int], visit:Set[int])->None:
            if len(p)==n:
                res.append(p[::])
                return 
            
            for i in range(n):
                num = nums[i]
                if num not in visit:
                    visit.add(num)
                    p.append(num)
                    backtrack(p, visit)
                    visit.remove(num)
                    p.pop()

        backtrack([], set())
        return res #n!