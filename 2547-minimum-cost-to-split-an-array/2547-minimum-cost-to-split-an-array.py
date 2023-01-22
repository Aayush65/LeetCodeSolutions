class Solution:
    def minCost(self, nums: List[int], k: int) -> int:
        memo = {}
        n = len(nums)    
        def rec(index: int) -> int:
            if index == n:
                return 0
            if index in memo:
                return memo[index]
            res = float("inf")
            hashmap = {}
            currTotal = 0
            for i in range(index, n):
                if nums[i] in hashmap:
                    hashmap[nums[i]] += 1
                    if hashmap[nums[i]] == 2:
                        currTotal += 1
                    currTotal += 1
                else:
                    hashmap[nums[i]] = 1
                res = min(res, currTotal + k + rec(i + 1))
            memo[index] = res
            return res

        return rec(0)