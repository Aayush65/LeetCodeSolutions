class Solution:
    def maxNumOfMarkedIndices(self, nums: List[int]) -> int:
        nums.sort()
        i, j = 0, ceil(len(nums)/2)
        while j < len(nums):
            if 2 * nums[i] <= nums[j]:
                i += 1
            j += 1
        return i * 2
        