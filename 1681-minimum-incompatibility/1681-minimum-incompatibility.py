class Solution:
    def minimumIncompatibility(self, nums: List[int], k: int) -> int:
        ''' Using preComputed subsets and dp '''

        size = len(nums) // k

        memo = {}
        def dp(nums: list[int]) -> int:
            if tuple(nums) in memo:
                return memo[tuple(nums)]
            if not nums:
                return 0
            res = float("inf")
            combs = combinations(set(nums), size)
            for comb in combs:
                nextNums = nums.copy()
                for i in comb:
                    nextNums.remove(i)
                score = max(comb) - min(comb)
                res = min(res, dp(nextNums) + score)
            memo[tuple(nums)] = res
            return res

        res = dp(nums)
        return -1 if res == float("inf") else res


        ''' Most Efficient Solution done using backtracking (optimised) and bitmasking. '''

        # maskMap = {}
        # maskIndices = {}
        # mask = 1
        # for i in sorted(list(set(nums))):
        #     maskMap[i] = mask
        #     maskIndices[mask] = i
        #     mask <<= 1

        # size = len(nums) // k
        # allSubs = [0] * k

        # def eleCount(num: int) -> int:
        #     count = 0
        #     while num:
        #         count += num & 1
        #         num >>= 1
        #     return count

        # def score(num: int) -> int:
        #     maxi = 0
        #     mini = float("inf")
        #     mask = 1
        #     for _ in range(16):
        #         if mask & num:
        #             mini = min(mini, mask)
        #             maxi = max(maxi, mask)
        #         mask <<= 1
        #     return maskIndices[maxi] - maskIndices[mini]

        # memo = {}
        # hits = 0
        # def backtrack(index: int) -> int:
        #     if (index, tuple(sorted(allSubs))) in memo:
        #         nonlocal hits
        #         hits += 1
        #         return memo[(index, tuple(sorted(allSubs)))]
        #     if index == len(nums):
        #         res = 0
        #         for i in allSubs:
        #             if eleCount(i) < size:
        #                 return float("inf")
        #             res += score(i)
        #         return res
        #     res = float("inf")
        #     mask = maskMap[nums[index]]
        #     for i in range(k):
        #         if allSubs[i] & mask or eleCount(allSubs[i]) == size:
        #             continue
        #         allSubs[i] ^= mask
        #         res = min(res, backtrack(index + 1))
        #         allSubs[i] ^= mask
        #     memo[(index, tuple(sorted(allSubs)))] = res
        #     return res

        # res = backtrack(0)
        # print("Hits: ", hits)
        # return -1 if res == float("inf") else res