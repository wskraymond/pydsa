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
        '''
            normal case 1: ()())()
            normal case 2: (())()

            edge case 1: )()()(()()))
            edge case 2: )(

            idea: 
                we don't know if a open bracket is valid or not until an invalid close bracket exists or end of line
            solution: 
                by storing index of unmatched bracket or -1 , we're able compute the length of longest valid parnetheses.
        '''
        stack = []
        res = 0
        
        for i,c in enumerate(s):
            if stack and c==')':
                top = stack.pop()
                if s[top] == '(':
                    last_index = stack[-1] if stack else -1
                    res = max(res, i-last_index)
                else: # new invalid bracket comes in
                    stack.append(i)
            else:
                stack.append(i)
        return res            

class solution_minus_1:
    def longestValidParentheses(self, s: str) -> int:
        res,stack = 0,[-1]
        for i,c in enumerate(s):
            top = stack[-1]
            if top > -1 and c == ')' and s[top] == '(':
                stack.pop() # pop matched one
                res = max(res, i-stack[-1])
            else:
                stack.append(i)
        return res