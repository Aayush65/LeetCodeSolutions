class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        mod = 1000000007
        
        @cache
        def dp(index: int, score: int) -> int:
            if index == len(nums):
                return 1
            res = dp(index + 1, score)
            if score + nums[index] < k:
                res += dp(index + 1, score + nums[index])
            return res % mod
        
        return max(2 ** len(nums) - 2 * dp(0, 0), 0) % mod