class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
#         memo = {len(nums): 0}
#         def dfs(index: int):
#             if index in memo:
#                 return memo[index]
#             length = 0
#             for i in range(index, len(nums)):
#                 if nums[i] > nums[index]:
#                     length = max(length, dfs(i))
#             length += 1
#             memo[index] = length
#             return length
            
#         maxLen = 0
#         for i in range(len(nums)):
#             maxLen = max(maxLen, dfs(i))
#         return maxLen

        dp = [0] * len(nums)
        dp[len(nums) - 1] = 1
        for i in range(len(nums) - 2, -1, -1):
            prevMax = 0
            for j in range(len(nums) - 1, i, -1):
                if nums[j] > nums[i]:
                    prevMax = max(prevMax, dp[j])
            dp[i] = prevMax + 1
        return max(dp)