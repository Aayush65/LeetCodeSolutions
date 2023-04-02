class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        maxLen = 0
        zeros = 0
        ones = 0
        for i in range(len(s)):
            if ones and s[i] == '0':
                zeros = 0
                ones = 0
            if s[i] == '0':
                zeros += 1
            else:
                ones += 1
            maxLen = max(maxLen, 2 * min(zeros, ones))
        return maxLen