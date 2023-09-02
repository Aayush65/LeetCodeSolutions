class Solution:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:
        n = len(nums)
        
        eleMap = {}
        total = 0
        for i in range(k):
            total += nums[i]
            if nums[i] not in eleMap:
                eleMap[nums[i]] = 0
            eleMap[nums[i]] += 1
        
        res = total if len(eleMap) >= m else 0
        
        for i in range(n - k):
            eleMap[nums[i]] -= 1
            if not eleMap[nums[i]]:
                del eleMap[nums[i]]
            if nums[i + k] not in eleMap:
                eleMap[nums[i + k]] = 0
            eleMap[nums[i + k]] += 1
            
            total += nums[i + k] - nums[i]
            if len(eleMap) >= m:
                res = max(res, total)
        return res
            