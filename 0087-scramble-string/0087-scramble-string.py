class Solution:
    @cache
    def isScramble(self, s1: str, s2: str) -> bool:
        if Counter(s1) != Counter(s2):
            return False
        if len(s1) == 1:
            return True
        map1 = defaultdict(int)
        startMap = defaultdict(int)        
        endMap = defaultdict(int)
            
        for i in range(len(s1) - 1):
            map1[s1[i]] += 1
            startMap[s2[i]] += 1
            endMap[s2[-i - 1]] += 1
            if map1 == startMap and \
                self.isScramble(s1[:i + 1], s2[:i + 1]) and \
                self.isScramble(s1[i + 1:], s2[i + 1:]):
                return True
            if map1 == endMap and \
                self.isScramble(s1[:i + 1], s2[-i - 1:]) and \
                self.isScramble(s1[i + 1:], s2[:-i - 1]):
                return True
        return False