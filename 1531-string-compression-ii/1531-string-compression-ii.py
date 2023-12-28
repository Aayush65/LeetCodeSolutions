class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        
        @cache
        def dp(index: int, prev: str, prevCount: int, k: int) -> int:
            if index == len(s):
                return prevCount if prevCount < 2 else len(str(prevCount)) + 1
            if s[index] == prev:
                res = dp(index + 1, prev, prevCount + 1, k)
            else:
                res = prevCount if prevCount < 2 else len(str(prevCount)) + 1
                res += dp(index + 1, s[index], 1, k)
            if k:
                res = min(res, dp(index + 1, prev, prevCount, k - 1))
            return res
        
        return dp(0, '', 0, k)