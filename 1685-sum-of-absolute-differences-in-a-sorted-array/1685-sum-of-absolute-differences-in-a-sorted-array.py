class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        left, right = 0, sum(nums)
        res = []
        for i in range(len(nums)):
            score = nums[i] * i - left
            left += nums[i]
            right -= nums[i]
            score += right - nums[i] * (len(nums) - i - 1)
            res.append(score)
        return res