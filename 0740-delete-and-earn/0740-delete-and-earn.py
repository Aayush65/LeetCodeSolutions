class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        numsMap = {i: 0 for i in nums}
        for i in nums:
            numsMap[i] += 1
        nums = sorted(list(set(nums)))

        @cache
        def dp(index: int) -> int:
            if index == len(nums):
                return 0
            score = 0

            score = nums[index] * numsMap[nums[index]]
            if index + 1 < len(nums):
                if nums[index + 1] == nums[index] + 1:
                    score += dp(index + 2)
                    score = max(score, dp(index + 1))
                else:
                    score += dp(index + 1)

            return score

        return dp(0)