class Solution:
    def minOperations(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        total = 0
        preSum = []
        for i in nums:
            total += i
            preSum.append(total)

        res = []
        for query in queries:
            idx = bisect_left(nums, query)
            if idx == n or nums[idx] != query:
                idx -= 1
            if idx < 0:
                res.append(total - query * n)
            else:
                res.append(total - preSum[idx] - query * (n - idx - 2) + query * idx - preSum[idx])
        return res