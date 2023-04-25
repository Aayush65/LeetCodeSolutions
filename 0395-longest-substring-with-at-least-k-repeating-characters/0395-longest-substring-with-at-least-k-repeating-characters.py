class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        
        def rec(l: int, r: int) -> int:
            freqMap = [0] * 26
            indexOf = lambda x: ord(x) - ord('a')
        
            for i in range(l, r):
                freqMap[indexOf(s[i])] += 1
        
            for i in range(l, r):
                if freqMap[indexOf(s[i])] < k:
                    freqMap[indexOf(s[i])] -= 1
                    return max(rec(l, i), rec(i + 1, r))
            return r - l
        
        return rec(0, len(s))