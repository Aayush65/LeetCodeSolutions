class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # i = 0
        # j = len(nums) - 1
        # while i < j:
        #     m = (i + j) // 2
        #     if nums[m] < target:
        #         i = m + 1
        #     else:
        #         j = m
        # if j < 0 or nums[j] != target:
        #     return [-1, -1]
        # res = [j]
        # i = 0
        # j = len(nums) - 1
        # while i < j:
        #     m = (i + j + 1) // 2
        #     if nums[m] > target:
        #         j = m - 1
        #     else:
        #         i = m
        # return res + [i]
        
        left = bisect_left(nums, target)
        if left == len(nums) or nums[left] != target:
            return [-1, -1]
        right = bisect_right(nums, target)
        return [left, right - 1]