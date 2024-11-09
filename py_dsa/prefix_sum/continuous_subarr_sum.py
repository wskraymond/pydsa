from math import remainder
from typing import List
class Solution_bruteforce:
    '''
        Given an integer array nums and an integer k, return true if nums has a good subarray or false otherwise.

        A good subarray is a subarray where:

        its length is at least two, and
        the sum of the elements of the subarray is a multiple of k.

        Note that:

        A subarray is a contiguous part of the array.
        An integer x is a multiple of k if there exists an integer n such that x = n * k. 0 is always a multiple of k.
    '''
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        '''
            0 <= nums[i] <= 109
            0 <= sum(nums[i]) <= 231 - 1
            1 <= k <= 231 - 1
        '''
        n = len(nums)
        for size in range(2, n+1):
            for i,j in zip(range(n-size+1), range(size,n+1)):
                if sum(nums[i:j])%k==0:
                    return True
                
        return False

class Solution_prefix_sum_missing_size_check:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        '''
            a) its length is at least two, and
            b) the sum of the elements of the subarray is a multiple of k.
            
            solution) prefix_sum % k = remainder
        '''
        if len(nums) < 2:
            return False
         
        remainder_set = set([0])
        prefix_sum = nums[0]
        remainder_set.add(prefix_sum%k)
        
        for num in nums[1:]:
            prefix_sum += num
            if prefix_sum%k in remainder_set:
                return True
            else:
                remainder_set.add(prefix_sum%k)
        
        return False
    
class Solution_prefix_sum:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        '''
            Criteria
                a) its length is at least two, and
                b) the sum of the elements of the subarray is a multiple of k.
                c) 0 <= nums[i] <= 109

            solution: 
                1) prefix_sum % k = remainder
                2) map remainder to index of first ocurrance
        '''
        n = len(nums)
        m = { 0:-1 }
        prefix_sum = 0
        for i in range(n):
            prefix_sum+=nums[i]
            r = prefix_sum%k
            if r not in m:
                m[r]=i
            elif i - m[r]>=2:
                return True

        return False

