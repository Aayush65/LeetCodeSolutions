# class Solution:
#     def maxRunTime(self, n: int, batteries: List[int]) -> int:
#         batteries = [-i for i in batteries]
#         batteries.sort()
        
#         if len(batteries) < n:
#             return 0
#         comps = [0] * n
#         while batteries:
#             toChange = heappop(comps)
#             poped = -heappop(batteries)
#             toChange += poped
#             heappush(comps, toChange)
#         return comps[0]

class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        batteries.sort()
        su = sum(batteries)
        while batteries[-1] > su // n:
            n -= 1
            su -= batteries.pop()
        return su // n