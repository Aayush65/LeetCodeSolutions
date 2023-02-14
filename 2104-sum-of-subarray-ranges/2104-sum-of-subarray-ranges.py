class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)):
            mn = nums[i]
            mx = nums[i]
            for j in range(i + 1, len(nums)):
                mx = max(mx, nums[j])
                mn = min(mn, nums[j])
                res += mx - mn
        return res