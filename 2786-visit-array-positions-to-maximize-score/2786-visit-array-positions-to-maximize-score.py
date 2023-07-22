class Solution:
    def maxScore(self, nums: List[int], x: int) -> int:
        n = len(nums)
        
        @cache
        def dp(index: int, parity: int) -> int:
            if index == n:
                return 0
            notTake = dp(index + 1, parity)
            if nums[index] % 2 == parity:
                take = nums[index] + dp(index + 1, parity)
            else:
                take = nums[index] + dp(index + 1, 1 - parity) - x
            return max(take, notTake)
            
        return nums[0] + dp(1, nums[0] % 2)