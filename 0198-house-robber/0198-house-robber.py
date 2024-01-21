class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        maxCash = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            nums[i] += max(nums[i - 3] if i - 3 >= 0 else 0, nums[i - 2])
            maxCash = max(maxCash, nums[i])
        return maxCash