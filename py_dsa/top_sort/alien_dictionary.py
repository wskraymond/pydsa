from collections import defaultdict
from typing import List
class Solution_dfs:
    '''
     * You may assume all letters are in lowercase.
     * You may assume that if a is a prefix of b, then a must appear before b in the given dictionary.
     * If the order is invalid, return an empty string.
     * There may be multiple valid order of letters, return any one of them is fine.
    '''
    def alienOrder(self, words: List[str]) -> str:
        #adj list constructed by lexicographical order in dict
        adj = defaultdict(set)
        for i in range(len(words)-1):
            w1, w2 = words[i], words[i+1]
            n = min(len(w1), len(w2))
            for j in range(n):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break
            else:    
                if len(w1) > len(w2):
                    return "" # If the order is invalid, return an empty string.
        
        #post-order traversal
        color = defaultdict(lambda:'W')
        result = []
        def dfs(c:str) -> bool:
            color[c] = 'G'
            for neigbhour in adj[c]:
                if color[neigbhour]=='W':
                    if not dfs(neigbhour):
                        return False
                elif color[neigbhour]=='G':
                    return False
            # post-visit
            color[c] = 'B'
            result.append(c)
        
        #multiple tree
        for c in { w[i] for i in range(len(w)) for w in words }:
            if color[c]=='W':
                is_valid = dfs(c)
                if not is_valid:
                    return "" # If the order is invalid, return an empty string.
        
        #reverse list
        # in-place reverse
        result.reverse()
        
        return "".join(result)