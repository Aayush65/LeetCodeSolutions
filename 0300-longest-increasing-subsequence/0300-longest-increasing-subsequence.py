class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = {len(nums): 0}
        def dfs(index: int):
            if index in memo:
                return memo[index]
            length = 0
            for i in range(index, len(nums)):
                if nums[i] > nums[index]:
                    length = max(length, dfs(i))
            length += 1
            memo[index] = length
            return length
            
        maxLen = 0
        for i in range(len(nums)):
            maxLen = max(maxLen, dfs(i))
        return maxLen