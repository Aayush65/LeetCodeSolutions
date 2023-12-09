class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        freq = defaultdict(int)
        n = len(nums)
        i, maxLen = 0, 1
        for j in range(n):
            freq[nums[j]] += 1
            while freq[nums[j]] > k:
                freq[nums[i]] -= 1
                i += 1
            maxLen = max(maxLen, j - i + 1)
        return maxLen