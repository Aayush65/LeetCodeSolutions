class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        
        @cache
        def dp(index: int, time: int) -> int:
            if index == len(satisfaction):
                return 0
            if satisfaction[index] >= 0:
                res = 0
                for i in range(index, len(satisfaction)):
                    res += time * satisfaction[i]
                    time += 1
                return res
            res = max(dp(index + 1, time), satisfaction[index] * time + dp(index + 1, time + 1))
            return res
        
        return dp(0, 1)