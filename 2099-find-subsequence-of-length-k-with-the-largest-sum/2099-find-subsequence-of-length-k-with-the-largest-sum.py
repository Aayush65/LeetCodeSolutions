class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        nums = sorted([[nums[i], i] for i in range(len(nums))], reverse=True)[:k]
        nums.sort(key=lambda x: x[1])
        return [i[0] for i in nums]
        