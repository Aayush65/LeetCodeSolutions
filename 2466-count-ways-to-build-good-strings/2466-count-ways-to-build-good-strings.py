class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        count = 0
        dp = [0] * (high + 1)
        dp[0] = 1
        
        for i in range(high + 1):
            dp[i] += dp[i - zero] if i >= zero else 0
            dp[i] += dp[i - one] if i >= one else 0
            if i >= low:
                count += dp[i]

        return count % (10 ** 9 + 7) 