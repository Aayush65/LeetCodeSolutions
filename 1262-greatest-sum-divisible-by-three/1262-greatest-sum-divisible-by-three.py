class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        memo = {}

        def dp(index: int, score: int) -> int:
            if index == len(nums):
                return 0 if score == 0 else -float("inf")
            if (index, score) in memo:
                return memo[(index, score)]
            res = max(dp(index + 1, score), nums[index] + dp(index + 1, (score + nums[index]) % 3))
            memo[(index, score)] = res
            return res

        return dp(0, 0)