class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        
        @cache
        def dp(l: int, r: int) -> int:
            if l > r:
                return 0
            if l == r:
                return nums[l]
            ifLeft = min(dp(l + 2, r), dp(l + 1, r - 1)) + nums[l]
            ifRight = min(dp(l + 1, r - 1), dp(l, r - 2)) + nums[r]
            return max(ifLeft, ifRight)
        
        half = sum(nums) / 2
        return True if dp(0, len(nums) - 1) >= half else False