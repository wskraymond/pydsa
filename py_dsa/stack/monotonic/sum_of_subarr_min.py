from typing import List
class Solution:
    '''
        Given an array of integers arr, find the sum of min(b), 
        where b ranges over every (contiguous) subarray of arr. 

        Since the answer may be large, return the answer modulo 109 + 7.
    '''
    def sumSubarrayMins(self, arr: List[int]) -> int:
        '''
            idea:
                1. iterate every largest subarray having a unique min value across arr 
                    - it means that the subarray should be as large as it can contains all shorter subarray 
                        , which commonly has the same min value
                2. on each unique min subarr, how many subarray are there in it sharing the same min value
                    - no. of sub. sharing the same min(i) 
                      = (i - left+1) * (right-i+1) 
                3. How can we know the left and right for each largest subarray sharing the same unique min ?
                    - every element on arr is a min value, and for each of it, we have to know the next smaller left/right index
                    - then , we know the boundary of largest subarray sharing the same min value.
                
            what we missed:
                1. duplicate value:
                    min is actually not unique , but the largest subarry has to be unique 
                2. how can we make sure each is unique given duplicate value.
                    for 2 randomly selected duplicates, the subarray of each min won't include each other.
                    However , only either of them include another duplicate.
            
            Solution:
                1. A ascending mono stack from left to right
                    - pop element when arr[i] < top
                    - then (arr[i]>=top) , push to stack
                2. pop-based: 
                     a) popped element = min = j
                     b) arr[i] = next right smaller value = r
                     c) top element after popping = next left smaller/equal value = l
                        (here, duplicates are excluded on the left side)
                     d) if stack is empty after popping , there is no next left.
                        l = -1
                     e) remaining unpopped, there is no next right.
                        r = n
                3. counting
                    (j-l) * (r-j)
                4. return the answer in modulo 109 + 7.
                    sum += min*counting
                    return sum % 10^9 + 7

        '''
        M = int(1e9 +  7) # the expression 1e9+7 is interpreted as a floating-point number
        stack, n, sum = [], len(arr), 0
        for i,v in enumerate(arr):
            while stack and v < arr[stack[-1]]:
                r = i
                j = stack.pop()
                l = stack[-1] if stack else -1
                sum += arr[j]*(j-l)*(r-j)
            stack.append(i)
        
        #remaining unpopped
        while stack:
            r = n
            j = stack.pop()
            l = stack[-1] if stack else -1
            sum += arr[j]*(j-l)*(r-j)
                
        return sum%M