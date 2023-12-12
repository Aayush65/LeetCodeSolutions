class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums = sorted([i - 1 for i in nums])
        return max(nums[-1] * nums[-2], nums[0] * nums[1])