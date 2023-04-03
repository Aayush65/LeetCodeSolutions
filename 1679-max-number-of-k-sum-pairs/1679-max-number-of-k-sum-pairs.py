class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        pairs = 0
        i, j = 0, len(nums) - 1
        while i < j:
            if nums[i] + nums[j] > k:
                j -= 1
            elif nums[i] + nums[j] < k:
                i += 1
            else:
                j -= 1
                i += 1
                pairs += 1
        return pairs