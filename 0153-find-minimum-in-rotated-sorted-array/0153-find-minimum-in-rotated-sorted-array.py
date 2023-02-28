class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        i, j = 0, len(nums) - 1
        while i <= j:
            mid = (i + j) // 2
            if nums[mid] < nums[(mid - 1) % n]:
                return nums[mid]
            if nums[mid] >= nums[i] and nums[i] > nums[j]:
                i = mid + 1
            else:
                j = mid - 1
        return nums[(i + j)//2]