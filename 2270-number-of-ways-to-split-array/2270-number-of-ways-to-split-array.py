class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        preSum = []
        total = 0
        for i in nums:
            total += i
            preSum.append(total)
        preSum.pop()
        
        count = 0
        for i in preSum:
            if i >= total - i:
                count += 1
        return count