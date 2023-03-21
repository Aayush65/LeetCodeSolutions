class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        maxLen = 0
        currLen = 0
        lastChar = ''
        for i in s:
            if not lastChar or ord(i) == ord(lastChar) + 1:
                currLen += 1
                maxLen = max(maxLen, currLen)
            else:
                currLen = 1
            lastChar = i
        return maxLen