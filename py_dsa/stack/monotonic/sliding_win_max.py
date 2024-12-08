from typing import List
from collections import deque

class Solution:
    '''
        You are given an array of integers nums, there is a sliding window of size k 
        which is moving from the very left of the array to the very right.
        
        You can only see the k numbers in the window. Each time the sliding window moves right by one position.

        Return the max sliding window.
    '''
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        '''
            Constraints:
                1 <= nums.length <= 105
                -104 <= nums[i] <= 104
                1 <= k <= nums.length

            Goal: 
                we're gonna return a list of max value within every sliding window moving from left to right
            
            idea:
                1. how can we keep track of the max of k=sized subarray using O(1) access time
                    - the access of the bottom of a decreasing mono stack from left to right
                2. when should we pop to keep decreasing and the bottom is for current k-sized subarray
                    - pop the top when nums[i] > top 
                    - pop the bottom when (i - bottom index + 1) > k
                3. when do we start to put the max onto the answer list.
                    - after pushing k elements into stack
                    - for every element after K-1 , we pipe up to answers.
                4, what kind of data structure allows to pop the top and bottom using o(1)
                    - deque
        '''

        dsc_stack,n=deque(),len(nums)
        if n < k:
            raise ValueError(f"{n}<{k}")

        ans = []
        for i,v in enumerate(nums):
            while dsc_stack and v > nums[dsc_stack[-1]]:
                dsc_stack.pop()

            #stack could become empty
            dsc_stack.append(i)

            while dsc_stack[-1] - dsc_stack[0] + 1 > k:
                dsc_stack.popleft()
            
            if i + 1 >=k:
                ans.append(nums[dsc_stack[0]])
            
        return ans
        

class Solution_pop_bottom_using_left_pointer_j:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dsc_stack,n=deque(),len(nums)
        if n < k:
            raise ValueError(f"{n}<{k}")

        ans,j = [0]*(n-k+1),0
        for i,v in enumerate(nums):
            while dsc_stack and v > nums[dsc_stack[-1]]:
                dsc_stack.pop()

            #stack could become empty
            dsc_stack.append(i)

            if j > dsc_stack[0]: # if bottom index is smaller than left boundary of moving window
                dsc_stack.popleft()
            
            if i + 1 >=k:
                ans[j] = nums[dsc_stack[0]]
                j+=1
            
        return ans


        
