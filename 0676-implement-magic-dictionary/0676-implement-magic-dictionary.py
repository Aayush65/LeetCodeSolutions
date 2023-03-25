class MagicDictionary:

    def __init__(self):
        self.dictionary = defaultdict(list)
        
    def buildDict(self, dictionary: List[str]) -> None:
        for i in dictionary:
            self.dictionary[len(i)].append(i)
        
    def search(self, searchWord: str) -> bool:
        for i in self.dictionary[len(searchWord)]:
            if self.check(i, searchWord):
                return True
        return False
        
    def check(self, s1, s2):
        flag = 2
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                flag -= 1
            if flag < 1:
                return False
        return flag == 1

# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)