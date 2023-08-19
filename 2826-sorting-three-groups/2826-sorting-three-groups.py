class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        
        @cache
        def dp(index: int, mini: int):
            if index == len(nums):
                return 0
            if nums[index] == mini:
                return dp(index + 1, mini)
            res = 1 + dp(index + 1, mini)
            if nums[index] > mini:
                res = min(res, dp(index + 1, nums[index]))
            return res            
        
        return dp(0, 1)