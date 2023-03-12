class Solution:
    def maxScore(self, nums: List[int]) -> int:
        nums.sort(reverse = True)
        preSum = []
        total = 0
        for i in nums:
            total += i
            preSum.append(total)
        
        count = 0
        for i in preSum:
            if i > 0:
                count += 1
        return count