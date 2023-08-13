class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        
        @cache
        def dp(index: int) -> bool:
            if index == n:
                return True
            res = False
            if index + 1 < n and nums[index] == nums[index + 1]:
                res = dp(index + 2)
            if not res and index + 2 < n:
                if nums[index] == nums[index + 1] and nums[index] == nums[index + 2]:
                    res |= dp(index + 3)
                if not res and nums[index + 1] == nums[index] + 1 and nums[index + 2] == nums[index] + 2:
                    res |= dp(index + 3)
            return res
        
        return dp(0)