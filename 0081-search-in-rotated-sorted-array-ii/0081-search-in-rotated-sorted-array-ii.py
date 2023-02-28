class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        def find(i: int, j: int):
            mid = (i + j) // 2
            if nums[mid] == target:
                return True
            if j < i:
                return False
            if i == j:
                return nums[i] == target
            if nums[mid] == nums[i] and nums[mid] == nums[j]:
                return find(i, mid - 1) or find(mid + 1, j)
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
            return find(i, j)

        return find(0, n - 1)