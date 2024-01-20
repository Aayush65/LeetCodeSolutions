class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        target = sorted(nums[1:])
        return nums[0] + target[0] + target[1]