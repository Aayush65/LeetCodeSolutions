class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()

        memo = {}
        def dp(index: int, time: int) -> int:
            if index == len(satisfaction):
                return 0
            if (index, time) in memo:
                return memo[(index, time)]
            if satisfaction[index] >= 0:
                res = 0
                for i in range(index, len(satisfaction)):
                    res += time * satisfaction[i]
                    time += 1
                memo[(index, time)] = res
                return res
            res = max(satisfaction[index] * time + dp(index + 1, time + 1), dp(index + 1, time))
            memo[(index, time)] = res
            return res

        return dp(0, 1)