class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        mod = int(1e9 + 7)
        n = len(nums)
        reqs = [0] * (n + 1)
        for i, j in requests:
            reqs[i] += 1
            reqs[j + 1] -= 1
        
        reqs.pop()
        for i in range(1, n):
            reqs[i] += reqs[i - 1]
            
        reqs.sort()
        nums.sort()
        
        total = 0
        for i in range(n):
            total += reqs[i] * nums[i]
            total %= mod
        return total 