class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        i, j = 0, len(nums) - 1
        while i <= j:
            mid = (i + j) // 2
            if mid % 2 == 0:
                if mid < len(nums) - 1 and nums[mid] == nums[mid + 1]:
                    i = mid + 2
                elif mid > 0 and nums[mid] == nums[mid - 1]:
                    j = mid - 2
                else:
                    return nums[mid]
            else:
                if mid > 0 and nums[mid] == nums[mid - 1]:
                    i = mid + 1
                elif mid < len(nums) - 1 and nums[mid] == nums[mid + 1]:
                    j = mid - 1
                else:
                    return nums[mid]