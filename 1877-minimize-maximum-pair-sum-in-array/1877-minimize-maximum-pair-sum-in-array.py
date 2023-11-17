class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        res = 0
        for i in range(len(nums)):
            res = max(res, nums[i] + nums[-i - 1])
        return res