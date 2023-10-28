class Solution:
    def minChanges(self, s: str) -> int:
        n = len(s)
        count = 0
        for i in range(1, n, 2):
            if s[i] != s[i - 1]:
                count += 1
        return count