class Solution:
    def hasTrailingZeros(self, nums: List[int]) -> bool:
        flag = 2
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                flag -= 1
        return flag <= 0