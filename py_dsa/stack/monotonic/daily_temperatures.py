from typing import List
class Solution_insert_based:
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

        dsc_stack, n = [], len(temperatures)
        ans = [0]*n
        #for i,x in enumerate(reversed(temperatures)): #reverse value but not index
        for i in reversed(range(n)):
            x = temperatures[i]
            while dsc_stack and temperatures[dsc_stack[-1]] <= x:
                dsc_stack.pop()

            ans[i] = dsc_stack[-1] - i if dsc_stack else 0
            dsc_stack.append(i)
                
        return ans

class Solution_pop_based:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        '''
            a decreasing mono stack from left to right
            popped index will be answer's index
        '''
        dsc_stack,n = [], len(temperatures)
        ans = [0]*n
        for i, t in enumerate(temperatures):
            while dsc_stack and t > temperatures[dsc_stack[-1]]:
                j = dsc_stack.pop()
                ans[j] = i-j
            dsc_stack.append(i)
        
        #elmenets remaining in stack have no next greater value
        return ans