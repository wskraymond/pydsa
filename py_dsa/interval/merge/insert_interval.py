from typing import Callable, List

from py_dsa import interval
class Solution_one_on_one_forwarding:
    '''
        You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] 
        represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. 
        You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

        Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals 
        still does not have any overlapping intervals (merge overlapping intervals if necessary).

        Return intervals after the insertion.

        Note that you don't need to modify intervals in-place. You can make a new array and return it.
    '''
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        '''
            Constraints:
                0 <= intervals.length <= 104
                intervals[i].length == 2
                0 <= starti <= endi <= 105
                intervals is sorted by starti in ascending order.
                newInterval.length == 2
                0 <= start <= end <= 105
        '''

        '''
            Example 2: (equals(=) is regarded as overlapping)

                Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
                Output: [[1,2],[3,10],[12,16]]
                Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
        '''

        '''
            insertion scenario (one on one forwarding): newInterval=[s,e] vs interval[i]
                1. e < intervals[i][0]
                    append newInterval to res
                    then return res + intervals[i:]
                2. s > intervals[i][1]
                    append interval[i] to res
                3. else then overlapped
                    merge into 'newInterval' by 
                        - newInterval[0] = min(s , interval[i][0]) 
                        - newInterval[1] = max(e, interval[i][1])
                4. after iteration (not return in first case), 
                    append newInterval to res
                    return res
        '''
        n = len(intervals)
        res = []
        prev_merged = newInterval[:]
        for i in range(n):
            s,e = intervals[i]
            s2,e2 = prev_merged
            if e2 < s:
                res.append(prev_merged)
                return res + intervals[i:]
            elif s2 > e:
                res.append(intervals[i])
            else: #overlapped
                prev_merged[0] = min(s,s2)
                prev_merged[1] = max(e,e2)
            
        res.append(prev_merged)
        return res

class Solution_binary:
    # https://neetcode.io/solutions/insert-interval
    # https://leetcode.ca/2016-01-26-57-Insert-Interval
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n=len(intervals)
        s,e = newInterval

        #non-overlapped left part : O(logn)
        i,j=0,n-1
        left = -1
        while i<=j:
            mid=i+(j-i)//2
            e1 = intervals[mid][1]
            e2 = intervals[mid+1][1] if mid+1<n else float('inf')
            if e1 < s <= e2:
                left = mid
                break
            elif e1 < s:
                i = mid+1
            else:
                j = mid-1

        #non-overlapped right part : O(logn)      
        i,j=0,n-1
        right = n
        while i<=j:
            mid=i+(j-i)//2
            s1 = intervals[mid][0]
            s2 = intervals[mid-1][0] if mid-1>=0 else -1
            if s1 > e >= s2:
                right = mid
                break
            elif s1 > e:
                j = mid-1
            else:
                i = mid+1
        
        if left+1!=right:
            s = min(s, intervals[left+1][0])
            e = max(e, intervals[right-1][1])
        
        ''' alternative: (in-place) delete & insert
            del intervals[left+1:right-1]
            intervals.insert(left+1, [s,e])
            return intervals
        '''
    
        #copying: O(n)
        #totaL = 2*logn + n = O(n)
        return intervals[:left+1] + [[s,e]] + intervals[right:]
        
