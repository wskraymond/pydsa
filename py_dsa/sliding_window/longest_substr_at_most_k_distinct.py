from collections import Counter, defaultdict

class Solution_dict:
    '''
        * Given a string s and an integer k, return the length of the longest substring of s that contains at most k distinct characters.
        *
        *
        *
        * Example 1:
        *
        * Input: s = "eceba", k = 2
        * Output: 3
        * Explanation: The substring is "ece" with length 3.
        * Example 2:
        *
        * Input: s = "aa", k = 1
        * Output: 2
        * Explanation: The substring is "aa" with length 2.
        *
        *
        * Constraints:
        *
        * 1 <= s.length <= 5 * 104
        * 0 <= k <= 50
    '''
    def lengthOfLongestSubstringKDistinct(self, s: str, k:int) -> int:
        m_counter = {}
        i,j,n=0,0,len(s)
        res = 0
        for i in range(n):
            if s[i] not in m_counter:
                m_counter[s[i]] = 0
            m_counter[s[i]] += 1
            while j<=i and len(m_counter) > k:
                m_counter[s[j]] -= 1
                if m_counter[s[j]]==0:
                    del m_counter[s[j]]
                j+=1
            res = max(res, i-j+1)

        return res


class Solution_counter:
    def lengthOfLongestSubstringKDistinct(self, s: str, k:int) -> int:
        ctr = Counter()
        i,j=0,0
        res = 0
        for i,c in enumerate(s):
            ctr[c] += 1
            while len(ctr) > k:
                ctr[s[j]] -= 1
                if ctr[s[j]]==0:
                    ctr.pop(s[j])
                j+=1
            res = max(res, i-j+1)

        return res

class Solution_defaultdict:
    def lengthOfLongestSubstringKDistinct(self, s: str, k:int) -> int:
        if k==0:
            return 0
        
        m = defaultdict(int)
        res,j=0,0
        for i,c in enumerate(s):
            m[c]+=1
            while len(m) > k:
                c2 = s[j]
                m[c2]-=1
                if m[c2]==0:
                    m.pop(c2)
                j+=1
            res = max(res,i-j+1)
        return res