from typing import List
class Solution_1d:
    '''
    Given an array nums, return the maximum alternating sum of any 'subsequence' of nums (after reindexing the elements of the subsequence).
    '''
    def maxAlternatingSum(self, nums: List[int]) -> int:
        '''
            1. The alternating sum of a 0-indexed array is defined as the sum of the elements at even indices minus the sum of the elements at odd indices
            2. For example, the alternating sum of [4,2,5,3] is (4 + 5) - (2 + 3) = 4
        '''
        '''
            Recursion:
                f(i, 0) = max{ f(i+1, 1) + nums[i] , f(i+1, 0) } 
                f(i, 1) = max{ f(i+1, 0) - nums[i] , f(i+1, 1) }
            base case:
                f(n, 0) = 0
                f(n, 1) = 0
            Goal:
                f(0, 0)

        '''
        if not nums:
            return 0
        
        n = len(nums)
        '''
            Java: 
                In Java, if you use new int[n][m], it initializes an array where all values default to zero without explicitly setting them. 
                This is indeed an O(1) operation for creation
            Python:
                In Python, we don't have a similar construct that initializes arrays to zeros by default. We have to explicitly set each value, 
                leading to O(n * m) complexity
        '''
        dp = [[0]*2 for _ in range(n+1)] #Time: O(n) , Space: O(n)
        for i in range(n-1, -1,-1): #O(n)
            dp[i][0] = max(dp[i+1][1] + nums[i], dp[i+1][0])
            dp[i][1] = max(dp[i+1][0] - nums[i], dp[i+1][1])
        
        return dp[0][0] #Time: O(2n) = O(n) , Space: O(n)

class Solution:
    '''
    Given an array nums, return the maximum alternating sum of any 'subsequence' of nums (after reindexing the elements of the subsequence).
    '''
    def maxAlternatingSum(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        n = len(nums)
        odd, even = 0,0
        for i in range(n-1,-1,-1):
            #multiple assignment
            even,odd = max(odd + nums[i], even), max(even - nums[i], odd)
        return even