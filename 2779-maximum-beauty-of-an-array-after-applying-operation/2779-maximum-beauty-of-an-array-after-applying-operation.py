class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        maxLen = 0
        for i in range(n):
            borderIdx = bisect_right(nums, nums[i] + 2 * k)
            length = borderIdx - i
            maxLen = max(length, maxLen)
        return maxLen