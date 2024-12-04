from typing import List
class Solution:
    '''
        Given an array of integers temperatures represents the daily temperatures,
        
        return an array answer such that answer[i] is the number of days you have to wait 
        after the ith day to get a warmer temperature. 
        
        If there is no future day for which this is possible, keep answer[i] == 0 instead.
    '''
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        '''
            Insertion-based:
                0. A decreasing monotonic stack from right to left 
                1. x = temperature[i] = inserted element
                2. poping elements from stack till > x
                3. answer[i] = top element index - i = the number of days to get warmer
                4. if stack is empty, answer[i] = 0
        '''

        stack, n = [], len(temperatures)
        ans = [0]*n
        #for i,x in enumerate(reversed(temperatures)): #reverse value but not index
        for i in reversed(range(n)):
            x = temperatures[i]
            while stack and temperatures[stack[-1]] <= x:
                stack.pop()

            ans[i] = stack[-1] - i if stack else 0
            stack.append(i)
                
        return ans