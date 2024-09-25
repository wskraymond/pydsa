class Trie:
    class TreeNode:
        def __init__(self) -> None:
            self.child = {}
            self.isComplete = False

    def __init__(self):
        self.root = Trie.TreeNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for i in range(len(word))
            if word[i] not in curr.child:
                curr.child[word[i]] = Trie.TreeNode()
            curr = curr.child[word[i]]
        curr.isComplete = True    

    def search(self, word: str) -> bool:
        node = self.__find__(word)
        return node.isComplete if node else False

    def startsWith(self, prefix: str) -> bool:
        node = self.__find__(prefix)
        return node is not None

    def __find__(self, word: str):
        curr = self.root
        for i in range(len(word)):
            if word[i] not in curr.child:
                return None
            curr = curr.child[word[i]]
        return curr


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)