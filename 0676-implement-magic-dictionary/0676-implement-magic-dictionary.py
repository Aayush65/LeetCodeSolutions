class MagicDictionary:

    def __init__(self):
        self.dictionary = set()
        

    def buildDict(self, dictionary: List[str]) -> None:
        for i in dictionary:
            self.dictionary.add(i)
        
    def search(self, searchWord: str) -> bool:
        temp = list(searchWord)
        for i in range(len(temp)):
            for j in range(26):
                ch = chr(ord('a') + j)
                if ch == searchWord[i]:
                    continue
                temp[i] = ch
                if ''.join(temp) in self.dictionary:
                    return True
            temp[i] = searchWord[i]
        return False
        


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)