class Solution:
    @cache
    def isScramble(self, s1: str, s2: str) -> bool:
        if Counter(s1) != Counter(s2):
            return False
        if len(s1) == 1:
            return True
        map1 = [0] * 26
        startMap = [0] * 26        
        endMap = [0] * 26
        indexOf = lambda x: ord(x) - ord('a')
        
        for i in range(len(s1) - 1):
            map1[indexOf(s1[i])] += 1
            startMap[indexOf(s2[i])] += 1
            endMap[indexOf(s2[-i - 1])] += 1
            if map1 == startMap and \
                self.isScramble(s1[:i + 1], s2[:i + 1]) and \
                self.isScramble(s1[i + 1:], s2[i + 1:]):
                return True
            if map1 == endMap and \
                self.isScramble(s1[:i + 1], s2[-i - 1:]) and \
                self.isScramble(s1[i + 1:], s2[:-i - 1]):
                return True
        return False