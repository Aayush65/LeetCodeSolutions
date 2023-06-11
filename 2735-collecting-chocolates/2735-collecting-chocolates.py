class Solution:
    def minCost(self, nums: List[int], x: int) -> int:
        n = len(nums)
        bestPrices = nums.copy()
        totalCost = sum(nums)
        currCost = totalCost
        
        for shift in range(1, n):
            currCost += x
            for i in range(n):
                c1, c2 = bestPrices[i], nums[(i + shift) % n]
                if c2 < c1:
                    currCost += c2 - c1
                    bestPrices[i] = c2
            totalCost = min(totalCost, currCost)

        return totalCost
    
# 119