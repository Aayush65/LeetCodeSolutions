class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        maximum = nums[0]
        total = nums[0]
        for i in range(1, len(nums)):
            total += nums[i]
            maximum = max(maximum, (total + i)//(i+1))
        return maximum