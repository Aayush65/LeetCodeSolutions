class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            while 0 < nums[i] <= n and nums[i] != i + 1 and nums[nums[i] - 1] != nums[i]:
                temp = nums[i] - 1
                nums[i], nums[temp] = nums[temp], nums[i]

        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        return n + 1
