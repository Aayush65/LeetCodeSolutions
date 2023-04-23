class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        mod = 1000000007
        @cache
        def dp(index: int) -> int:
            if index == len(s):
                return 1
            res = 0
            currNum = 0
            for i in range(index, len(s)):
                currNum = currNum * 10 + int(s[i]) 
                if not currNum or currNum > k:
                    break
                res += dp(i + 1)
            return res % mod
            
        return dp(0)