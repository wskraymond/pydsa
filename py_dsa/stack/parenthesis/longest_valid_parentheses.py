class Solution:
    '''
        Given a string containing just the characters '(' and ')', return the length of the longest valid (well-formed) parentheses substring
    '''
    def longestValidParentheses(self, s: str) -> int:
        '''
            Constraints:
                0 <= s.length <= 3 * 104
                s[i] is '(', or ')'.
        '''
        stack = []
        n = len(s)
        res,count = 0,0
        for c in s:
            if c==')':
                if stack:
                   stack.pop()
                   count+=2
                   res = max(res, count)
                else:
                   count=0
            else:
                stack.append 
                 


        pass