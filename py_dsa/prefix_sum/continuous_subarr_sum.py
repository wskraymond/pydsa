from typing import List
class Solution:
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