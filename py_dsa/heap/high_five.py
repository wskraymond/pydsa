from collections import defaultdict
from typing import List
import heapq
class Solution:
    '''
    Return the answer as an array of pairs result, where result[j] = [IDj, topFiveAveragej] represents the student with IDj and their top five average. Sort result by IDj in increasing order.
    '''
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        '''
            items, where items[i] = [IDi, scorei] represents one score from a student with IDi
        '''
        #no java TreeMap in py standard libs
        #heapq only supports minheap
        scores_dict = defaultdict(list)
        for id, score in items:
            heapq.heappush(scores_dict[id], score)
            if len(scores_dict[id]) > 5:
                heapq.heappop(scores_dict[id])
        
        result = [ [id, sum(scores)//5 ] for id, scores in scores_dict.items() ]
        result.sort(key=lambda pair: pair[0])
        return result

class Solution_pre_sort:
    '''
    Return the answer as an array of pairs result, where result[j] = [IDj, topFiveAveragej] represents the student with IDj and their top five average. Sort result by IDj in increasing order.
    '''
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        '''
            items, where items[i] = [IDi, scorei] represents one score from a student with IDi
        '''
        #no java TreeMap in py standard libs
        #heapq only supports minheap
        scores_dict = defaultdict(list)
        for id, score in items:
            heapq.heappush(scores_dict[id], score)
            if len(scores_dict[id]) > 5:
                heapq.heappop(scores_dict[id])
        
        result = [ [id, sum(scores_dict[id])//5 ] for id in sorted(scores_dict.keys()) ]
        return result