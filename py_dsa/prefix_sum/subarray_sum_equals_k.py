from collections import defaultdict
from typing import List
class Solution_bruteforce:
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
    
class Solution_prefix_sum:
    '''
        Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.
    '''
    def subarraySum(self, nums: List[int], k: int) -> int:
        '''
            criteria:
                a) both value and k could be negative
                    - subarray sum could be zero 
                    - more than one subarray (adjacent) have the same value of sum
            
            solution:
                1) a - b = k
                2) map prefix sum to count (increment when found)
                3) iterate every prefix , we know how many number of value b exists so that a - b = k
                    - result = sum up all count 
        '''

        m = {0:1}
        result, prefix_sum = 0, 0
        for num in nums:
            prefix_sum+=num
            b = prefix_sum - k
            if b in m:
                result+=m[b]
            
            if prefix_sum not in m:
                m[prefix_sum]=1
            else:
                m[prefix_sum]+=1

        return result

class Solution_prefix_sum_default_dict:
    def subarraySum(self, nums: List[int], k: int) -> int:
        '''
            criteria:
                a) both value and k could be negative
                    - subarray sum could be zero 
                    - more than one subarray (adjacent) have the same value of sum
            
            solution:
                1) a - b = k
                2) map prefix sum to count (increment when found)
                3) iterate every prefix , we know how many number of value b exists so that a - b = k
                    - result = sum up all count 
        '''

        m = defaultdict(int)
        m[0]=1
        result, prefix_sum = 0, 0
        for num in nums:
            prefix_sum+=num
            b = prefix_sum - k
            
            result+=m[b]
            m[prefix_sum]+=1

        return result