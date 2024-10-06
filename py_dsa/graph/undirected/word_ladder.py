from collections import defaultdict, deque
from typing import List
class Solution_exact_graph_by_iterating_26:
    '''
        Given two words, beginWord and endWord, and a dictionary wordList, 
        return the number of words in the shortest transformation sequence from beginWord to endWord, 
        or 0 if no such sequence exists.
    '''
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        '''
        *     1 <= beginWord.length <= 10
        *     endWord.length == beginWord.length
        *     1 <= wordList.length <= 5000
        *     wordList[i].length == beginWord.length
        *     beginWord, endWord, and wordList[i] consist of lowercase English letters.
        *     beginWord != endWord
        *     All the words in wordList are unique.
        '''
        '''
        #wordList constraint
        *     Every adjacent pair of words differs by a single letter.
        *     Every si for 1 <= i <= k is in wordList. 
                Note that beginWord does not need to be in wordList.
        *     sk == endWord
        '''
        if not wordList or endWord not in wordList:
            return 0
        #n,m = len(wordList), len(wordList[0])
        # adj constructed by iterating a-z on every char of a word
        # n x m x 26
        # exact mapping graph
        s = set(wordList+[beginWord])
        adj = defaultdict(list)
        for w in s:
            for i in range(len(w)):
                for j in range(ord('a'), ord('z')+1):  #alternatively, for letter in string.ascii_lowercase:
                    if w[i] == chr(j):
                        continue
                    next = w[:i] + chr(j) + w[i+1:]
                    if next in s:
                        adj[w].append(next)
        
        #bfs to find shortest path
        # O()
        q = deque([beginWord])
        visit = set([beginWord])
        res = 0
        while q:
            res +=1
            for _ in range(len(q)):
                w = q.popleft()
                if w==endWord:
                    return res
                for neighbour in adj[w]:
                    if neighbour not in visit:
                        q.append(neighbour)
                        visit.add(neighbour)
                    
        return 0

class Solution_wildcard_mapping:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if wordList is None or endWord not in wordList:
            return 0
        
        #adj: reversely, we map the known word to all of its wild card pattern
        # O(n*m^2)
        adj = defaultdict(list)
        for w in wordList + [beginWord]: #O(n)
            for i in range(len(w)):      #O(m)
                adj[w[:i] + '*' + w[i+1:]].append(w) #O(m)
        
        #bfs: traverse from its wildcard pattern to next vertices
        #O(V+E) * O(m) = O(n^2 * m)
        q = deque([beginWord])
        visit = set([beginWord])
        res = 0
        while q:    #O(V)
            res+=1
            for _ in range(len(q)):
                w = q.popleft()
                if w == endWord:    #O(m)
                    return res
                for j in range(len(w)): #O(m)
                    for neighbour in adj[w[:j] + '*' + w[j+1:]]: # O(E)
                        if neighbour not in visit:
                            visit.add(neighbour)
                            q.append(neighbour)
        return 0    #As n >> m , O(n^2 * m)
