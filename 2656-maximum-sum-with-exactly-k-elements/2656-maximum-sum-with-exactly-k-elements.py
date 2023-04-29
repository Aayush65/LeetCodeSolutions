class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        nums.sort()
        m = nums[-1]
        res = 0
        for i in range(k):
            res += m
            m += 1
        return res