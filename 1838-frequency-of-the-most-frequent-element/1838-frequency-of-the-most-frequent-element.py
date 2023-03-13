class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        i, j = 0, 0
        total = 0
        maxWindow = 1
        while j < len(nums):
            if (j - i) * nums[j] <= total + k:
                total += nums[j]
                j += 1
            else:
                total -= nums[i]
                i += 1
            maxWindow = max(maxWindow, j - i)
        return maxWindow