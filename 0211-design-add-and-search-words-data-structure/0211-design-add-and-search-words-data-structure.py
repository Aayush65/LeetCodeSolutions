class WordDictionary:

    def __init__(self):
        self.child = {}
        self.isWord = False

    def addWord(self, word: str) -> None:
        curr = self
        for i in word:
            if i not in curr.child:
                curr.child[i] = WordDictionary()
            curr = curr.child[i]
        curr.isWord = True

    def search(self, word: str) -> bool:

        def dfs(index: int, root: WordDictionary) -> bool:
            curr = root
            for i in range(index, len(word)):
                if word[i] == '.':
                    for j in curr.child.values():
                        if dfs(i + 1, j):
                            return True
                    return False
                if word[i] not in curr.child:
                    return False
                curr = curr.child[word[i]]
            return curr.isWord
        
        return dfs(0, self)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)