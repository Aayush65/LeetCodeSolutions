class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        maxSum = 0
        n = len(nums)
        for i in range(1, n + 1):
            total = 0
            for j in range(1, n + 1):
                nextEle = i * j * j
                if nextEle > n:
                    break
                total += nums[nextEle - 1]
            maxSum = max(maxSum, total)
        return maxSum