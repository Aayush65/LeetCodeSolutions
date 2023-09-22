class Trie:
    def __init__(self):
        self.children = {}
        self.topThree = []
        self.isWord = False
        
    def addWord(self, string: str) -> None:
        curr = self
        word = string.s
        for i in word:
            if i not in curr.children:
                curr.children[i] = Trie()
            curr = curr.children[i]
            # adding to topThree
            heappush(curr.topThree, string)
            if len(curr.topThree) > 3:
                heappop(curr.topThree)
        curr.isWord = True

class MyString:
    def __init__(self, s):
        self.s = s
        
    def __lt__(self, s2):
        return self.s > s2.s
    
    def __eq__(self, s2):
        return self.s == s2.s
    
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        tr = Trie()
        for word in products:
            tr.addWord(MyString(word))

        res = []
        curr = tr
        for i in searchWord:
            if (res and not res[-1]) or i not in curr.children:
                res.append([])
            else:
                curr = curr.children[i]
                res.append(sorted([i.s for i in curr.topThree]))
        return res