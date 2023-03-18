class Solution:
    def maximizeGreatness(self, nums: List[int]) -> int:
        nums.sort()
        i = j = 0
        while j < len(nums):
            if nums[j] == nums[i]:
                j += 1
            else:
                j += 1
                i += 1
        return i