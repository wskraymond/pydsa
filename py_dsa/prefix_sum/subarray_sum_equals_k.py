from typing import List
class Solution:
    '''
        Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.
    '''
    def subarraySum(self, nums: List[int], k: int) -> int:
        '''
            -1000 <= nums[i] <= 1000
            -107 <= k <= 107
        '''

        n = len(nums)
        count = 0
        for size in range(1,n+1):
            for i,j in zip(range(n-size+1), range(size,n+1)):
                if sum(nums[i:j])==k:
                    count+=1
        return count