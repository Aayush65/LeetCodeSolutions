class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        res = 0
        n = len(nums)
        for i in range(n):
            hs = set()
            for j in range(i, n):
                hs.add(nums[j])
                res += len(hs) ** 2
        return res
                