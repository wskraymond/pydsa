from typing import List
class Solution:
    '''
        A triplet is an array of three integers. You are given a 2D integer array triplets, where triplets[i] = [ai, bi, ci] describes the ith triplet. You are also given an integer array target = [x, y, z] that describes the triplet you want to obtain.

        To obtain target, you may apply the following operation on triplets any number of times (possibly zero):

        Choose two indices (0-indexed) i and j (i != j) and update triplets[j] to become [max(ai, aj), max(bi, bj), max(ci, cj)].
            For example, if triplets[i] = [2, 5, 3] and triplets[j] = [1, 7, 5], triplets[j] will be updated to [max(2, 1), max(5, 7), max(3, 5)] = [2, 7, 5].
        
        Return true if it is possible to obtain the target triplet [x, y, z] as an element of triplets, or false otherwise.
    '''
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        '''
            template:
                1. candidate set
                2. selectin function
                3. feasibility function
                4. objective function
                5. solution function
            idea:
                1. Triplets[i]
                2. one iteration ( order doesn't matter for triplets[i][j] )
                3. check if triplets[i] <= target
                4. add the index of matched numbers to the set
                    (i.e numbers in target can be duplicates)
                5. return len(set) == 3
        '''

        matches = set() # store unique index for target
        for triplet in triplets:
            if all( a <= b for a,b in zip(triplet, target)):
                for i in range(0, len(target)):
                    if triplet[i] == target[i]:
                        matches.add(i)
        return len(matches)==3

class Solution_arr:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        k = len(target)
        res = 0
        for triplet in triplets:
            matches = 0
            isValid = 0
            for i in range(0,k):
                if triplet[i] <= target[i]:
                    isValid |= 1<<i
                    if triplet[i] == target[i]:
                        matches |= 1<<i
            if isValid == 7:
                res |= matches
        return res==7
        