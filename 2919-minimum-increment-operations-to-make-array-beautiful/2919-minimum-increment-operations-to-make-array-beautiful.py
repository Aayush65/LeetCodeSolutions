class Solution:
    def minIncrementOperations(self, nums: List[int], k: int) -> int:
        count = 0

        memo = {}
        def dp(index: int) -> int:
            curr = tuple(nums[index: index + 3])
            if (index, curr) in memo:
                return memo[(index, curr)]
            if index >= len(nums) - 2:
                return 0
            if max(curr) >= k:
                return dp(index + 1)
            
            res = float("inf")
            for i in range(index, index + 3):
                diff = k - nums[i]
                nums[i] = k
                res = min(res, diff + dp(i + 1))
                nums[i] -= diff
            
            memo[(index, curr)] = res
            return res
            
        return dp(0)