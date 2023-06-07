class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        numsMap = {i: 0 for i in nums}
        for i in nums:
            numsMap[i] += 1
        nums = sorted(list(set(nums)))

        memo = {}
        visited = set()

        def dp(index: int) -> int:
            if index == len(nums):
                return 0
            if nums[index] - 1 in visited:
                return dp(index + 1)
            if index in memo:
                return memo[index]

            visited.add(nums[index])
            score = dp(index + 1) + nums[index] * numsMap[nums[index]]
            visited.remove(nums[index])
            
            score = max(score, dp(index + 1))
            memo[index] = score
            return score

        return dp(0)