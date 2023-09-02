class Solution:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:
        n = len(nums)
        
        preSum = [0]
        for i in nums:
            preSum.append(preSum[-1] + i)
    
        eleMap = {}
        for i in range(k):
            if nums[i] not in eleMap:
                eleMap[nums[i]] = 0
            eleMap[nums[i]] += 1
        
        res = preSum[k] if len(eleMap) >= m else 0
        
        for i in range(n - k):
            eleMap[nums[i]] -= 1
            if not eleMap[nums[i]]:
                del eleMap[nums[i]]
            if nums[i + k] not in eleMap:
                eleMap[nums[i + k]] = 0
            eleMap[nums[i + k]] += 1
            if len(eleMap) >= m:
                res = max(res, preSum[i + k + 1] - preSum[i + 1])
        return res
            