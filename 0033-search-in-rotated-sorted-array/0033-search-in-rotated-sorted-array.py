class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i, j = 0, len(nums) - 1
        while i <= j:
            mid = (i + j) // 2
            if nums[mid] < target:
                if nums[i] > target or nums[mid] >= nums[i]:
                    i = mid + 1
                else:
                    j = mid - 1
            elif nums[mid] > target:
                if nums[j] < target or nums[mid] <= nums[j]:
                    j = mid - 1
                else:
                    i = mid + 1
            else:
                return mid
        return -1
