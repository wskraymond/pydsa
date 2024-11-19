from typing import List

class Solution:
    '''
        There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].

        You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station to its next (i + 1)th station. You begin the journey with an empty tank at one of the gas stations.

        Given two integer arrays gas and cost, return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1. If there exists a solution, it is guaranteed to be unique.
    '''
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        '''
            Criteria:
                a) sum of gas - sum of cost >=0
                b) current accumulated gas at index i >= cost[i] 
                c) clockwise direction
            Solution:
                1) Positive(Any>0): iterating the suffix[j:] sum for every sub sum > 0 (Postive), sum+=gas[i]-cost[i]
                2) Net Negative: the longest suffix sum should cover the short(Negative) of the gas in prefix sum
                3) Net: suffix[j:] >= -prefix[:j] , then prefix[:j] + suffix[j:] >=0 , Genrally, prefix_sum >=0
                4) Example: sum(subarry[0:k]) + sum(subarry[k:j]) + sum(suffix[j:])
                   both sum(subarry[0:k]) and sum(subarry[k:j]) is negative
                   sum(suffix[j:]) is all positive iteratively till end
                
        '''

        n = len(gas)
        j = 0
        prefix_sum = 0
        suffix_Sum = 0
        for i in range(n):
            diff=gas[i]-cost[i]
            prefix_sum+=diff
            if suffix_Sum + diff < 0: 
                j=i+1 # reset
                suffix_Sum=0
            else:
                suffix_Sum+=diff
                
        return j if j<n and prefix_sum >=0 else -1
    

class Solution_2:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) - sum(cost) < 0:
            return -1
        
        n = len(gas)
        suffix_sum = 0
        j = 0
        for i in range(n):
            suffix_sum += gas[i] - cost[i]
            if suffix_sum < 0:
                j = i+1
                suffix_sum = 0
        return j