from typing import List
class Solution_bruteforce:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        '''
            storing complement in map/set won't help us , becos we're not gonna find equality , but smaller/larger triplets
            how to bruteforce every unique combination of 3 values
        '''

        n = len(nums)
        res = 0
        for i in range(n):
            for j in range(i+1,n):
                for k in range(j+1,n):
                    if nums[i] + nums[j] + nums[k] < target:
                        res+=1    
        return res
    
class Solution_double_counting:
    '''
        Given an array of n integers nums and an integer target, 
        find the number of index triplets i, j, k with 0 <= i < j < k < n 
        that satisfy the condition nums[i] + nums[j] + nums[k] < target.

        n == nums.length
        0 <= n <= 3500
        -100 <= nums[i] <= 100
        -100 <= target <= 100
    '''
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        '''
            Input: nums = [-2,0,1,3], target = 2
            Output: 2
            Explanation: Because there are two triplets which sums are less than 2:
            [-2,0,1]
            [-2,0,3]
        '''

        '''
            criteria:
                a) -100 <= nums[i] <= 100
                b) -100 <= target <= 100
                c) 0 <= i < j < k < n
            Solution:
                1) nums[j] + nums[k] < target - nums[i]
                2) sort: nlogn
                3) for each i, 2-pointers to find sum < target - nums[i]  
                    - if nums[j] + nums[k] < target - nums[i], then count+= k-j
                    - n^2
        '''

        arr, n = sorted(nums), len(nums)
        res = 0
        for i in range(n):
            j,k,x=0,n-1, target-arr[i]
            while j<k:
                if j==i:
                    j+=1
                elif k==i:
                    k-=1
                else:
                    sum = arr[j]+arr[k]
                    if sum >= x:
                        k-=1
                    else:
                        res+=k-j
                        j+=1
        return res
    
class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        '''
            criteria:
                a) -100 <= nums[i] <= 100
                b) -100 <= target <= 100
                c) 0 <= i < j < k < n
            Solution:
                1) nums[j] + nums[k] < target - nums[i]
                2) sort: nlogn
                3) to check every unique combination: nC3
                    for each i, 2-pointers to find sum < target - nums[i]
                    - 2 pointers at j=i+1 , k=n-1 to avoid duplicate   
                    - if nums[j] + nums[k] < target - nums[i], then count+= k-j => so we don't need to do one more iteration 
                    - n^2
        '''

        arr, n = sorted(nums), len(nums)
        res = 0
        for i in range(n):
            j,k,x=i+1,n-1, target-arr[i]
            while j<k:
                sum = arr[j]+arr[k]
                if sum >= x:
                    k-=1
                else:
                    res+=k-j
                    j+=1
        return res