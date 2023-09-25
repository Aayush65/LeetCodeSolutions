class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        hm = [0] * 26
        for i in s:
            hm[ord(i) - ord('a')] += 1
        for i in t:
            index = ord(i) - ord('a')
            if hm[index]:
                hm[index] -= 1
            else:
                return i