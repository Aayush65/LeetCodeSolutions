class Solution:
    def lengthOfLongestSubsequence(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        
        memo = {}
        def dp(index: int, total: int) -> int:
            if (index, total) in memo:
                return memo[(index, total)]
            if total == 0:
                return 0
            if index == n or total < nums[index]:
                return -float("inf")
            res = max(1 + dp(index + 1, total - nums[index]), dp(index + 1, total))
            memo[(index, total)] = res
            return res
            
            
        res = dp(0, target)
        memo.clear()
        return res if res != -float("inf") else -1