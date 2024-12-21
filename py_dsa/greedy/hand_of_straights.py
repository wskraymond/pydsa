from typing import List
import heapq
from collections import Counter, defaultdict
class Solution_counter:
    '''
        Alice has some number of cards and she wants to rearrange the cards into groups so that each group is of size groupSize, and consists of groupSize consecutive cards.
        Given an integer array hand where hand[i] is the value written on the ith card and an integer groupSize, return true if she can rearrange the cards, or false otherwise.
    '''
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        '''
            Constraints:
                1 <= hand.length <= 104
                0 <= hand[i] <= 109
                1 <= groupSize <= hand.length
        '''

        '''
            Example 1:

            Input: hand = [1,2,3,6,2,3,4,7,8], groupSize = 3
            Output: true
            Explanation: Alice's hand can be rearranged as [1,2,3],[2,3,4],[6,7,8]
        '''

        '''
            idea: Gready (to group a subarray of size=S as many as possible)
                1. for next new group , start from the smallest value(count > 0) in the remaining elements to make sure we won't miss any number in between groups.
                2. given a head number(x) for a group, how can we know if this group has S consecutive numbers for it, and how can we make sure a constant time for retrieval and update operation for k = x + 1 
                3. when we should stop (mismatched group exists) and how do we know we can continue .

            Solution:
                0. n = input array size, n%s = 0 And unique number = M
                1. O(n + nlogn): use min heap to keep track of the smallest number (M unique number) on the top , and pop the number on the top , when its count reaches zero.
                2. O(n): a {number -> count} map to keep track of the count for each unique number
                3. a) when the count of a number(k) reaches zero , but the smallest number on the top != k. It implies that the number on the top still remains but there will be missing consecutive number for next group, 
                        then we don't need to continue, even the current group has S consecutive.
                   b) Or, when the map doesn't contain ki=kj+1 (count=0)
        '''
        n,s = len(hand), groupSize
        if n%s!=0:
            return False

        num_counter = Counter(hand) #O(n)
        min_heap = list(num_counter.keys())     #O(n)
        heapq.heapify(min_heap) #O(n)

        while min_heap: #(nlogn)
            x = min_heap[0]
            for i in range(x,x+s):
                if i in num_counter:
                    num_counter[i]-=1  #O(1)
                else:
                    return False

                if num_counter[i]==0:
                    if min_heap[0]!=i:
                        return False
                    heapq.heappop(min_heap)
        return True

class Solution_map:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n,s = len(hand), groupSize
        if n%s!=0:
            return False

        num_counter = defaultdict(int)
        for num in hand:
            num_counter[num]+=1
        
        min_heap = list(num_counter.keys())     #O(n)
        heapq.heapify(min_heap) #O(n)

        while min_heap: #(nlogn)
            x = min_heap[0]
            for i in range(x,x+s):
                if i in num_counter:
                    num_counter[i]-=1  #O(1)
                else:
                    return False

                if num_counter[i]==0:
                    if min_heap[0]!=i:
                        return False
                    heapq.heappop(min_heap)
        return True
                