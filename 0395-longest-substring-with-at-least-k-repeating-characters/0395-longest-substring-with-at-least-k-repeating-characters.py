class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        maxLen = 0
        freqMap = [0] * 26
        indexOf = lambda x: ord(x) - ord('a')
        
        for i in s:
            freqMap[indexOf(i)] += 1
        
        for i in range(len(s)):
            if freqMap[indexOf(s[i])] < k:
                freqMap[indexOf(s[i])] -= 1
                return max(self.longestSubstring(s[:i], k), self.longestSubstring(s[i + 1:], k))
        return len(s)