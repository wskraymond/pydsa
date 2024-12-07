from typing import List

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
            
                
        '''

