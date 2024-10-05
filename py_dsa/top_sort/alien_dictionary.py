from collections import defaultdict, deque
from queue import Empty
from typing import List
class Solution_dfs_default_dict:
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
            return True
        
        #multiple tree
        for c in { w[i] for w in words for i in range(len(w)) }:
            if color[c]=='W':
                is_valid = dfs(c)
                if not is_valid:
                    return "" # If the order is invalid, return an empty string.
        
        #reverse list
        # in-place reverse
        result.reverse()
        
        return "".join(result)

class Solution_dfs:
    '''
     * You may assume all letters are in lowercase.
     * You may assume that if a is a prefix of b, then a must appear before b in the given dictionary.
     * If the order is invalid, return an empty string.
     * There may be multiple valid order of letters, return any one of them is fine.
    '''
    def alienOrder(self, words: List[str]) -> str:
        #adj list constructed by lexicographical order in dict
        ''' 
            if there are duplicate characters (c) across different words, 
            the dictionary will only keep the last occurrence of each character. 
            This means that earlier entries with the same key will be overwritten.
        '''
        adj = { c: set() for w in words for c in w } 
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
            return True
        
        #multiple tree
        for c in adj:
            if color[c]=='W':
                is_valid = dfs(c)
                if not is_valid:
                    return "" # If the order is invalid, return an empty string.
        
        #reverse list
        # in-place reverse
        result.reverse()
        
        return "".join(result)

class Solution_bfs_defaultdict:
    '''
     * You may assume all letters are in lowercase.
     * You may assume that if a is a prefix of b, then a must appear before b in the given dictionary.
     * If the order is invalid, return an empty string.
     * There may be multiple valid order of letters, return any one of them is fine.
    '''
    def alienOrder(self, words: List[str]) -> str:
        adj = { c:set() for w in words for c in w}
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
        
        # in_degree accumulated by counting every neighbour in adj
        in_degree = defaultdict(lambda:0)
        for neighbours in adj.values():
            for node in neighbours:
                in_degree[node] += 1
        
        #enqueue every zero-degree node to accomodate multiple tree
        q = deque([ c for c in adj if not in_degree[c] ])

        # add node in bfs order when in_degree is deducted to zero
        result = []
        while q:
            c = q.popleft()
            result.append(c)
            for neighbour in adj[c]:
                in_degree[neighbour] -=1
                if in_degree[neighbour]==0:
                    q.append(neighbour)

        # detect cycle: return reusult if all is valid
        return "".join(result) if all(degree==0 for degree in in_degree.values()) else ""

class Solution_bfs:
    '''
     * You may assume all letters are in lowercase.
     * You may assume that if a is a prefix of b, then a must appear before b in the given dictionary.
     * If the order is invalid, return an empty string.
     * There may be multiple valid order of letters, return any one of them is fine.
    '''
    def alienOrder(self, words: List[str]) -> str:
        adj = { c:set() for w in words for c in w}
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
        
        # in_degree accumulated by counting every neighbour in adj
        in_degree = {}
        for neighbours in adj.values():
            for node in neighbours:
                if node in in_degree:
                    in_degree[node] +=1
                else:
                    in_degree[node] = 1
        
        #enqueue every zero-degree node to accomodate multiple tree
        q = deque([ c for c in adj if c not in in_degree])

        # add node in bfs order when in_degree is deducted to zero
        result = []
        while q:
            c = q.popleft()
            result.append(c)
            for neighbour in adj[c]:
                in_degree[neighbour] -=1
                if in_degree[neighbour]==0:
                    q.append(neighbour)
                    in_degree.pop(neighbour)

        # detect cycle: return reusult if all is valid
        return "".join(result) if not in_degree else ""
