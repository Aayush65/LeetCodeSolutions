class Solution:
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        preSum = [0]
        for i in nums:
            preSum.append(preSum[-1] + i)
            
        memo = {}
        def dp(index: int, k: int) -> float:
            if (index, k) in memo:
                return memo[(index, k)]
            if index == len(nums):
                return 0
            if k == 0:
                return (preSum[-1] - preSum[index]) / (len(nums) - index)
            res = 0
            for i in range(index, len(nums)):
                res = max(res, (preSum[i + 1] - preSum[index]) / (i + 1 - index) + dp(i + 1, k - 1))
            memo[(index, k)] = res
            return res
        
        return dp(0, k - 1)