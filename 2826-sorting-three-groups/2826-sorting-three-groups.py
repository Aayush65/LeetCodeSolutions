class Solution:
    def minimumOperations(self, nums: List[int]) -> int:

        @cache
        def dp(index: int, prev: int) -> int:
            if index == len(nums):
                return 0
            res = dp(index + 1, prev)
            if nums[index] >= prev:
                res = max(res, 1 + dp(index + 1, nums[index]))
            return res
        
        return len(nums) - dp(0, 1)