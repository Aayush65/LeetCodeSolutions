# class Solution:
#     def stoneGameV(self, stoneValue: List[int]) -> int:
#         preSum = []
#         total = 0
#         for i in stoneValue:
#             total += i
#             preSum.append(total)
#         n = len(stoneValue)
        
#         @cache
#         def dp(l: int, r: int) -> int:
#             if l == r:
#                 return 0
#             res = 0
#             for i in range(l, r):
#                 leftPartition = preSum[i] - preSum[l - 1] if l > 0 else preSum[i]
#                 rightPartition = preSum[r] - preSum[i]
#                 if 2 * min(leftPartition, rightPartition) > res:
#                     if leftPartition > rightPartition:
#                         score = rightPartition + dp(i + 1, r)
#                     elif leftPartition < rightPartition:
#                         score = leftPartition + dp(l, i)
#                     else:
#                         scoreLeft = leftPartition + dp(l, i)
#                         scoreRight = rightPartition + dp(i + 1, r)
#                         score = max(scoreLeft, scoreRight)
#                     res = max(score, res)
#             return res
        
#         return dp(0, n - 1)
from itertools import accumulate
from bisect import bisect_left
from functools import cache

class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:

        sv = [0, *accumulate(stoneValue)]

        @cache
        def helper(fro, to):
            if to - fro == 1:
                return 0

            mid = bisect_left(sv, (sv[to] + sv[fro]) // 2)

            dist = res = 0
            explore_more = True
            while explore_more:
                explore_more = False
                for i in  [mid - dist, mid + dist]: 
                    if fro < i <= to:
                        left, right = sv[i] - sv[fro], sv[to] - sv[i]
                        if res // 2 <= left <= right:
                            res = max(res, left + helper(fro, i))
                            explore_more = True
                        if left >= right >= res // 2:
                            res = max(res, right + helper(i, to))
                            explore_more = True
                dist += 1
            return res

        return helper(0, len(stoneValue))