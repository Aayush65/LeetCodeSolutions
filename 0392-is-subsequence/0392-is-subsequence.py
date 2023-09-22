class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        j = 0
        for i in t:
            if j == len(s):
                break
            if i == s[j]:
                j += 1
        return j == len(s)
