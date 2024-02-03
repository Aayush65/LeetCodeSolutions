class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        preSum = [0]
        for i in nums:
            preSum.append(preSum[-1] + i)
        
        maxSum = -float("inf")
        hm = {}
        for i, x in enumerate(nums):
            if x + k in hm:
                maxSum = max(maxSum, preSum[i + 1] - hm[x + k])
            if x - k in hm:
                maxSum = max(maxSum, preSum[i + 1] - hm[x - k])
            if x not in hm:
                hm[x] = float("inf")
            hm[x] = min(preSum[i], hm[x])
        return maxSum if maxSum != -float("inf") else 0