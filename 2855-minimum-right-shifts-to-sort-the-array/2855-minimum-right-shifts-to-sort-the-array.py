class Solution:
    def minimumRightShifts(self, nums: List[int]) -> int:
        sarr = sorted(nums)
        if sarr == nums:
            return 0
        for i in range(len(nums)):
            if sarr == nums[i:] + nums[:i]:
                return len(nums) - i
        return -1