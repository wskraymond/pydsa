class Solution:
    '''
    Given a non-negative integer x, return the square root of x rounded down to the nearest integer. 
    '''
    def mySqrt(self, x: int) -> int:
        '''
        Constraints:
            0 <= x <= 2^31 - 1
        '''
        i,j = 0, x
        while i <=j:
            mid = i+(j-i)//2
            if mid*mid <= x < (mid+1)*(mid+1): # Multiple Comparison Operators
                return mid
            elif mid*mid > x:
                j = mid -1
            else:
                i = mid + 1
        '''
        No post-processing required because at each step, 
        you are checking to see if the element has been found.
        If you reach the end, then you know the element is not found
        '''
        raise Exception("not found")