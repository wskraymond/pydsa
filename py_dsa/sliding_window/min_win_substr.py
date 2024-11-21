from collections import Counter
class Solution_full_scan:
    '''
        Given two strings s and t of lengths m and n respectively, return the minimum window substring
        of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

        The testcases will be generated such that the answer is unique.
    '''
    def minWindow(self, s: str, t: str) -> str:
        '''
            1 <= m, n <= 105
            s and t consist of uppercase and lowercase English letters.

            Input: s = "a", t = "aa"
            Output: ""
            Explanation: Both 'a's from t must be included in the window.
            Since the largest window of s only has one 'a', return empty string.

            Follow up: Could you find an algorithm that runs in O(m + n) time?
        '''

        m,n = len(s) , len(t)

        if m < n:
            return ""
        
        t_ctr = Counter(t) #O(n)
        s_ctr = Counter()
        win_size,start,end = m+1,0,0
        j = 0
        for i,c in enumerate(s): #O(m)
            s_ctr[c]+=1
            if i >= n-1:
                while s_ctr >= t_ctr: #O(26 * 2) for uppercase and lowercase English letters.
                    if i - j + 1 < win_size:
                        start,end=j,i+1
                        win_size = end - start
                    s_ctr[s[j]]-=1
                    j+=1
        return s[start:end]
    

class Solution_compute_counter_if_present:
    def minWindow(self, s: str, t: str) -> str:
        '''
            General idea:
                1. use a map to store the key to remaining number of chars that is not yet satisfied (i.e it can be over-statisfied - negative)
                2. shrink(shift j forward) to approch the miminum of window size till the condition is no longer met
                3. use of a counter to keep track of how many chars in the string 't' we meet

            Tricks:
                a) value in the map{letter -> count } has to handle over-satisfied window , so the value has to go negative once over-satisified
                        - when shrinking , pointer j has to move out of over-satisifed letter and uncovered letters before reaching one satisfied letter(counter+=1)
                b) when window is shrinking after we had met the all letters in t at first time (counter=0), if s[j] is present in the map, then we keep iteration the counter size from 1 to 0.
                        - Thus, we don't need worry about how many duplicate char per each letter in t, becos pointer i will keep moving forward to deduct the counter from only 1 to zero iteratively
        '''
        m,n = len(s), len(t)
        if m < n:
            return ""
        
        t_ctr,counter = Counter(t),n
        l,start,end = float("inf"), 0,0
        j=0

        '''
            t_ctr[c] could be negative (oversatified)
        '''
        for i,c in enumerate(s):
            t_ctr[c]-=1 #substract even if it is not present
            if t_ctr[c]>=0: #decrement only if subtracted from positive
                counter-=1
            while counter==0:
                if i-j+1 < l:
                    start,end = j,i+1
                    l = end - start
                t_ctr[s[j]]+=1 #increment even if it is not present
                if t_ctr[s[j]]>0: #increment only if added to larger than zero
                    counter+=1
                j+=1
        return s[start:end]
    
class Solution_compute_counter_if_present_2:
    def minWindow(self, s: str, t: str) -> str:
        '''
            to keep the space complexity to be O(n) only
        '''
        m,n = len(s), len(t)
        if m < n:
            return ""
        
        t_ctr,counter = Counter(t),n
        l,start,end = float("inf"), 0,0
        j=0
        for i,c in enumerate(s):
            if c in t_ctr: #only present in t
                t_ctr[c]-=1
                if t_ctr[c]>=0:
                    counter-=1
            
            while counter==0:
                if i-j+1 < l:
                    start,end = j,i+1
                    l = end - start
                if s[j] in t_ctr: #only present in t
                    t_ctr[s[j]]+=1
                    if t_ctr[s[j]]>0:
                        counter+=1
                j+=1
        return s[start:end]
        
        




