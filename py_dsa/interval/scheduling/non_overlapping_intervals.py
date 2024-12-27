from typing import List

class Solution:
    '''
        Given an array of intervals intervals where intervals[i] = [starti, endi], 
        return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

        Note that intervals which only touch at a point are non-overlapping. 
        For example, [1, 2] and [2, 3] are non-overlapping.
    '''
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        '''
            Constraints:
                1 <= intervals.length <= 105
                intervals[i].length == 2
                -5 * 104 <= starti < endi <= 5 * 104
        '''

        '''
            idea: be greedy to remove the intervals which locally overlaps more intervals 
                1. candidate set: 
                    intervals
                2. selection function:
                    sort by start time asc
                3. feasibility function
                    if previous_non_conflict_end_time <= interval[0]
                        non-conflict: previous_non_conflict_end_time = interval[1]
                    else 
                        conflict: previous_non_conflict_end_time = interval[1] 
                            if interval[1] < previous_non_conflict_end_time 
                            else previous_non_conflict_end_time
                4. objective function
                    if conflict: count+=1
                5. solution function
                    return count
        '''

        intervals.sort(key=lambda x:x[0])
        prev_end = intervals[0][1]
        count=0
        for i in range(1,len(intervals)):
            start,end = intervals[i]
            if prev_end <= start:
                prev_end = end
            else:
                if end < prev_end:
                    prev_end = end
                count+=1
        return count
    

class Solution_2:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[0])
        prev_end = intervals[0][1]
        count = 0
        for i in range(1,len(intervals)):
            start,end = intervals[i]
            if prev_end > start: #overlapped
                prev_end = min(prev_end,end)
                count+=1
            else:
                prev_end = end
        return count