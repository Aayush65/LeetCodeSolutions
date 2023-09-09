class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        hashmap = {}
        def dfs(target: int) -> None:
            if target == 0:
                return 1
            if target in hashmap:
                return hashmap[target]
            res = 0
            for i in range(len(nums)):
                if nums[i] <= target:
                    res += dfs(target - nums[i])
            hashmap[target] = res
            return res
        return dfs(target)