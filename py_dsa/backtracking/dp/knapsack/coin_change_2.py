from typing import List
class Solution_2d_i_k:
    '''
        Return the number of combinations that make up that amount. 
        If that amount of money cannot be made up by any combination of the coins, return 0.
    '''
    def change(self, amount: int, coins: List[int]) -> int:
        '''
            You may assume that you have an infinite number of each kind of coin.
        '''

        '''
            recurrence relation:
                f(i, k) = f(i, k-coins[i]) if k >= coins[i] + f(i+1, k)
            base case:
                f(i,0) = 1
                f(i, k<0) = 0
            goal:
                f(0, S)
        '''
        n,s = len(coins), amount
        #  The slicing notation dp[:][0] = 1 doesn’t do what you might expect because dp[:] creates a shallow copy of the list, not a direct reference to the original elements
        dp = [[1] + [0]*s for _ in range(n+1)]

        for k in range(1,s+1):
            for i in range(n-1,-1,-1):
                dp[i][k] = ( dp[i][k-coins[i]] if k>=coins[i] else 0 ) + dp[i+1][k]

        return dp[0][s]

class Solution_2d_k_i:
    '''
        Return the number of combinations that make up that amount. 
        If that amount of money cannot be made up by any combination of the coins, return 0.
    '''
    def change(self, amount: int, coins: List[int]) -> int:
        '''
            You may assume that you have an infinite number of each kind of coin.
        '''

        '''
            recurrence relation:
                f(k, i) = f(k-coins[i], i) if k >= coins[i] + f(k, i+1)
            base case:
                f(0, i) = 1
                f(k<0, i) = 0
            goal:
                f(S, 0)
        '''
        n,s = len(coins), amount
        #  The slicing notation dp[:][0] = 1 doesn’t do what you might expect because dp[:] creates a shallow copy of the list, not a direct reference to the original elements
        '''
            However , dp[0][:] = [1]*(n+1) , 
            [1]*(n+1) creates a temporary list with n + 1 elements, all set to 1. This list is then used to update dp[i][:] in place. 
            It’s a short-lived temporary list just for the assignment. Efficient enough for most purposes!
        '''
        dp = [[0]*(n+1) for _ in range(s+1)]
        dp[0][:] = [1] * (n+1)

        for k in range(1,s+1):
            for i in range(n-1,-1,-1):
                dp[k][i] = ( dp[k-coins[i]][i] if k>=coins[i] else 0 ) + dp[k][i+1]

        return dp[s][0]
    
class Solution_1d_siginificant_top_order:
    '''
        Return the number of combinations that make up that amount. 
        If that amount of money cannot be made up by any combination of the coins, return 0.
    '''
    def change(self, amount: int, coins: List[int]) -> int:
        '''
            You may assume that you have an infinite number of each kind of coin.
        '''

        '''
            recurrence relation:
                f(i, k) = f(i, k-coins[i]) if k >= coins[i] + f(i+1, k)
            base case:
                f(i,0) = 1
                f(i, k<0) = 0
            goal:
                f(0, S)
        '''
        n,s = len(coins), amount
        dp = [1] + [0]*s
        
        # top order for i and j iteration here is significant for 1D array
        # so we cannot swap (iterate i first then k, otherwise we will lose the f(i, k-coins[i]) value , which dp[k-coins[i]] is no longer retained at i-th version)
        for i in range(n-1, -1,-1):
            for k in range(1,s+1):
                dp[k] = (dp[k-coins[i]] if k>=coins[i] else 0) + dp[k]
        return dp[s]