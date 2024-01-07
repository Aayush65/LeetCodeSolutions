class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        dp = [{} for i in nums]
        ans = 0
        for i in range(len(nums)):
            for j in range(i):
                diff = nums[i] - nums[j]
                if diff in dp[j]:
                    ans += dp[j][diff]
                    if diff in dp[i]:
                        dp[i][diff] += dp[j][diff] + 1
                    else:
                        dp[i][diff] = dp[j][diff] + 1
                else:
                    if diff in dp[i]:
                        dp[i][diff] += 1
                    else:
                        dp[i][diff] = 1
        return ans