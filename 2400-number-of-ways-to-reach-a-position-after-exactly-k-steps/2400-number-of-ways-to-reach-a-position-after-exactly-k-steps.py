class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        memo = {}

        def dp(pos: int, steps: int) -> int:
            if (pos, steps) in memo:
                return memo[(pos, steps)]
            if k == steps:
                if pos == endPos and k == steps:
                    return 1
                return 0
            res = 0
            if pos < endPos and endPos - pos < k or pos >= endPos:
                res += dp(pos - 1, steps + 1)
            if pos > endPos and pos - endPos < k or pos <= endPos:
                res += dp(pos + 1, steps + 1)
            memo[(pos, steps)] = res
            return res
            
        return dp(startPos, 0) % 1000000007