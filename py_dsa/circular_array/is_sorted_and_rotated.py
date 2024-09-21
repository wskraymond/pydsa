
from typing import List

class Solution:
    def check(self, nums: List[int]) -> bool:
        count, n = 0, len(nums)
        for i in range(n):
            j = i + 1 if i<n-1 else 0
            if nums[j] < nums[i]:
                count +=1
        return count <=1
