class Solution_2d_i_s:
    '''
        Given a string s, find the longest palindromic subsequence's length in s.
    '''
    def longestPalindromeSubseq(self, s: str) -> int:
        '''
            Recurrence Relation:
                f(i,j) = max( f(i+1,j-1) + 2 if s[i]==s[j], f(i+1,j) , f(i,j-1) ) | i <= j
            Base case:
                f(i,j=i) = 1
            Goal:
                f(0,n-1) 

            Top Order:
                for i=n-1....0
                    for s=2...n
        '''
        n = len(s)
        dp = [ [0]*i + [1] + [0]*(n-i-1)  for i in range(n)]
        for i in range(n-1,-1,-1):
            for j in range(i+1,n):
                if s[i]==s[j]:
                    dp[i][j] = (dp[i+1][j-1] if i+1<=j-1 else 0) + 2
                
                dp[i][j] = max(dp[i][j], dp[i+1][j], dp[i][j-1])
        return dp[0][n-1]
    
class Solution_2d_s_i:
    '''
        Given a string s, find the longest palindromic subsequence's length in s.
    '''
    def longestPalindromeSubseq(self, s: str) -> int:
        '''
            Recurrence Relation:
                f(i,j) = max( f(i+1,j-1) if i+1<=j-1 + 2 if s[i]==s[j] , f(i+1,j) , f(i,j-1) ) | i <= j
            Base case:
                f(i,j=i) = 1
            Goal:
                f(0,n-1) 

            Top Order:
                for size=2...n
                    for i=0...n-size , j = size-1...n-1
        '''
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1

        for size in range(2, n+1): #beware: size should include n (inclusive)  
            for i, j in zip(range(n - size + 1), range(size - 1, n)):
                dp[i][j] = max(
                    (dp[i + 1][j - 1] if i + 1 <= j - 1 else 0)  # actually, here even i+1>j-1 , we won't get index out of bound error becos it is n x n 2D arr
                    + (2 if s[i] == s[j] else 0),
                    dp[i + 1][j],
                    dp[i][j - 1],
                )
        return dp[0][n - 1]
                