from typing import List

class Solution:
    '''
    Given an integer array nums, find a subarray
    that has the largest product, and return the product.

    The test cases are generated so that the answer will fit in a 32-bit integer.
    '''
    def maxProduct(self, nums: List[int]) -> int:
        '''
        Constraints:
            1 <= nums.length <= 2 * 104
            -10 <= nums[i] <= 10
            The product of any subarray of nums is guaranteed to fit in a 32-bit integer.
        '''

        '''
            Criteria:
                a) nums[i] could be Negative , Zero
                b) -1 x -1 = positive
            Thought:
                1) neg_product = Min(val, neg_product * val, pos_product * val)    
                2) pos_product = Max(val, pos_product * val,  neg_product * val)
                3) max = Max(max, pos_product) 
            General Solution:
                0) neg_product could be the same as pos_product 
                   both could be -ve, 0 , +ve
                    min_p = Min(val, min_p*val, max_p*val)
                    max_p = Max(val, min_p*val, max_p*val)
                i) max could be negative or zero
                    Init: max = nums[0]
                    but still start iteration from index 0 
                2) 1 x val = val itself , so 1 is neutral
                    Init: max_p, min_p = 1, 1
                3) 0 x val = 0 , so 0 will reset everything
                    result = Max(max, max_p)
        '''
        
        res, min_p, max_p = nums[0], 1, 1
        for num in nums:
            min_p, max_p = min(num, min_p*num, max_p*num), max(num, min_p*num, max_p*num)
            res = max(res, max_p)

        return res

class Solution2:
    def maxProduct(self, nums: List[int]) -> int:
        # we could also init all 3 variables to first element
        res, min_p, max_p = nums[0], nums[0], nums[0]
        for num in nums[1:]: # if len(nums) < 2 , then nums[1:] returns empty list
            min_p, max_p = min(num, min_p*num, max_p*num), max(num, min_p*num, max_p*num)
            res = max(res, max_p)

        return res