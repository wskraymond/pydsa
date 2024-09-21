from typing import List

'''
Given an integer array nums of length n where all the integers of nums are in the range [1, n] and each integer appears once or twice, return an array of all the integers that appears twice.

You must write an algorithm that runs in O(n) time and uses only constant auxiliary space, excluding the space needed to store the output

'''
class BruteForce:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        result = []
        n = len(nums)
        for i in range(n):
            for j in range(i+1,n):
                if nums[i]==nums[j]:
                    result.append(nums[i])
        return result
    
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        i, n =0, len(nums)
        while i < n :
            j = nums[i]
            if nums[j-1]!=j: # if to-location(nums[j-1]) doesn't have corresponding value (j)
                #swap
                nums[i]=nums[j-1]
                nums[j-1]=j
            else:
                i+=1
        
        res = []
        for i in range(n): # find duplicates
            if nums[i]!=i+1:
                res.append(nums[i])
        return res
