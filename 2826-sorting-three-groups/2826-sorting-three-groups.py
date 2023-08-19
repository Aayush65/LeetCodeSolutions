class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        
        memo = [[-1] * 3  for i in range(len(nums))]
        
        def dp(index: int, mini: int) -> int:
            if index == len(nums):
                return 0
            if memo[index][mini - 1] != -1:
                return memo[index][mini - 1]
            if nums[index] == mini:
                return dp(index + 1, mini)
            res = 1 + dp(index + 1, mini)
            if nums[index] > mini:
                res = min(res, dp(index + 1, nums[index]))
            memo[index][mini - 1] = res
            return res            
        
        return dp(0, 1)