class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        dp1 = [0] * n
        for i in range(1, n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp1[i] = max(dp1[i], 1 + dp1[j])

        dp2 = [0] * n
        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                if nums[j] < nums[i]:
                    dp2[i] = max(dp2[i], 1 + dp2[j])

        res = 0
        for i in range(n):
            if dp1[i] and dp2[i]:
                res = max(res, dp1[i] + dp2[i] + 1)

        return n - res
