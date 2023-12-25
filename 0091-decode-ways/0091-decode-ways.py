class Solution:
    def numDecodings(self, s: str) -> int:
        memo = { len(s):1 }

        def dpNumDecoding(i:int):
            if i in memo:
                return memo[i]
            if s[i] == '0':
                return 0
            ways = dpNumDecoding(i+1)
            if i+1 < len(s) and 9 < int(s[i]+s[i+1]) < 27:
                ways += dpNumDecoding(i+2)
            memo[i] = ways
            return ways

        return dpNumDecoding(0)