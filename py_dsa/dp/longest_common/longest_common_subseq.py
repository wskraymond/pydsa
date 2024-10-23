class Solution_clone:
    '''
        Given two strings text1 and text2, return the length of their longest common subsequence. 
        If there is no common subsequence, return 0.
    '''
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        '''
            recurrence relation:
                f(i,j) = max( f(i+1,j+1) + 1 if text1[i]==text2[j], f(i+1,j), f(i,j+1) )
            base case:
                f(i=n,j) = 0
                f(i,j=m) = 0
            goal:
                f(0,0)
            top order:
                for i=n-1...0
                    for j=m-1...0
        '''

        n,m = len(text1), len(text2)
        curr = [0]*(m+1)
        prev = curr[::]
        for i in reversed(range(n)):
            for j in reversed(range(m)):
                curr[j] = max(
                    (prev[j + 1] + 1) if text1[i] == text2[j] else 0,
                    curr[j + 1],
                    prev[j],
                ) 
            prev = curr[::]
        return curr[0]
    
class Solution_swap:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text1) < len(text2): 
            text1, text2 = text2, text1 #swap

        n,m = len(text1), len(text2)
        curr = [0]*(m+1)
        prev = curr[::]
        for i in reversed(range(n)):
            for j in reversed(range(m)):
                curr[j] = max(
                    (prev[j + 1] + 1) if text1[i] == text2[j] else 0,
                    curr[j + 1],
                    prev[j],
                ) 
            curr, prev = prev, curr #swap
        return prev[0]  #beware!!