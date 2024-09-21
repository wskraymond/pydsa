from typing import List
class BruteForce:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n==0:
            return
        
        k%=n
        for i in range(k):
            last = nums[n-1]
            for j in reversed(range(1, n)):
                nums[j] = nums[j-1]
            else:
                nums[0] = last

class ReverseArray_tmp1:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k%=n
        nums[:] = nums[-k:] + nums[:-k] # replace all elements in the original nums with 2 newly created reversed list combined

        #space complexity = O(n)


class ReverseArray_tmp2:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k%=n
        # reverse() in-place operation o(1)
        nums.reverse()
        # slicing creates a new list when converted from the iterator, resulting in ( O(n) ) space complexity.
        nums[:k] = reversed(nums[:k])
        nums[k:] = reversed(nums[k:])

class RotateArray1:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k%=n
        def reverse(i, j):
            while i < j :
                tmp = nums[i]
                nums[i] = nums[j]
                nums[j] = tmp
                i+=1
                j-=1
        reverse(0, n-1)
        reverse(0, k-1)
        reverse(k, n-1)

class RotateArray2:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k%=n
        def reverse(i, j):
            while i < j :
                # multiple assignment without explicit tmp variable 
                nums[i], nums[j] = nums[j] , nums[i]
                i, j = i+1, j-1
        reverse(0, n-1)
        reverse(0, k-1)
        reverse(k, n-1)