class Solution:
    def destroyTargets(self, nums: List[int], space: int) -> int:
        multipleMap = {i % space: 0 for i in nums}
        for i in nums:
            multipleMap[i % space] += 1
        
        maxDestroyed = multipleMap[nums[0] % space]
        seed = nums[0]
        for i in nums:
            if multipleMap[i % space] > maxDestroyed:
                maxDestroyed = multipleMap[i % space]
                seed = i
            elif multipleMap[i % space] == maxDestroyed:
                seed = min(i, seed)
        return seed