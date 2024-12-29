from typing import List
class Solution_linear:
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
            insertion scenario (one to one scenario): newInterval=[s,e] vs interval[i]
                1. e <= intervals[i][0]
                    append newInterval to res
                    then return res + intervals[i:]
                2. s >= intervals[i][1]
                    append interval[i] to res
                3. else then overlapped
                    merge into 'newInterval' by 
                        - newInterval[0] = min(s , interval[i][0]) 
                        - newInterval[1] = max(e, interval[i][1])
                4. after iteration (not return in first case), 
                    append newInterval to res
                    return res
        '''
        pass

class Solution_binary:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        #Intervals Array is sorted. Can you use Binary Search to find the correct position to insert the new Interval.?
        pass