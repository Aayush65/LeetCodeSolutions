class Solution:
    def secondsToRemoveOccurrences(self, s: str) -> int:
        s = [int(i) for i in s]
        resTime = 0
        while True:
            isChanged = False
            i = 1
            while i < len(s):
                if s[i] == 1 and s[i - 1] == 0:
                    s[i - 1], s[i] = 1, 0
                    i += 1
                    isChanged = True
                i += 1
            if not isChanged:
                break
            resTime += 1
        return resTime