class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        nums = [(nums[i], cost[i]) for i in range(len(nums))]
        nums.sort()
        n = sum(i[1] for i in nums)
        
        def calcCost(val: int) -> int:
            cost = 0
            for i, j in nums:
                cost += abs(val - i) * j
            return cost
        
        if n % 2:
            currN = 0
            for i, j in nums:
                currN += j
                if currN > n // 2:
                    return calcCost(i)
        else:
            currN = 0
            res = float("inf")
            for i, j in nums:
                currN += j
                if currN >= n // 2:
                    res = min(res, calcCost(i))
                if currN > n // 2:
                    return min(res, calcCost(i))