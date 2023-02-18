class Solution:
    def minImpossibleOR(self, nums: List[int]) -> int:
        nums = set(nums)
        ans = 1
        while ans in nums:
            ans *= 2
        return ans