class Solution:
    def findValueOfPartition(self, nums: List[int]) -> int:
        nums.sort()
        minDiff = float("inf")
        for i in range(len(nums) - 1):
            minDiff = min(minDiff, nums[i + 1] - nums[i])
        return minDiff