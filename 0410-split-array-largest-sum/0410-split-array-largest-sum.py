class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        memo = {}
        def dfs(index: int, splits: int) -> int:
            if (index, splits) in memo:
                return memo[(index, splits)]
            if index == len(nums):
                return 0
            if splits == k:
                return float("inf")
            total = 0
            minRes = float("inf")
            for i in range(index, len(nums)):
                total += nums[i]
                res = max(total, dfs(i + 1, splits + 1))
                if total > minRes:
                    break
                minRes = min(res, minRes)
            memo[(index, splits)] = minRes
            return minRes
        
        return dfs(0, 0)