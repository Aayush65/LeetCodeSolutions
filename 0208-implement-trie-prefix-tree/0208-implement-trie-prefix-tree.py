class Trie:

    def __init__(self):
        self.child = {}
        self.isWord = False

    def insert(self, word: str) -> None:
        curr = self
        for i in word:
            if i not in curr.child:
                curr.child[i] = Trie()
            curr = curr.child[i]
        curr.isWord = True

    def search(self, word: str) -> bool:
        curr = self
        for i in word:
            if i not in curr.child:
                return False
            curr = curr.child[i]
        return curr.isWord

    def startsWith(self, prefix: str) -> bool:
        curr = self
        for i in prefix:
            if i not in curr.child:
                return False
            curr = curr.child[i]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)