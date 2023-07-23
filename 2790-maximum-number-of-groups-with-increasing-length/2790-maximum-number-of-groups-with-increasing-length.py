class Solution:
    def maxIncreasingGroups(self, usageLimits: List[int]) -> int:
        # usageLimits.sort(reverse=True)
        n = len(usageLimits)
        
#         def check(val: int) -> int:
#             h = [-val]
#             for i in usageLimits:
#                 tempI = i
#                 while tempI > 0 and h:
#                     largest = -heappop(h)
#                     largest, tempI = largest - tempI, tempI - largest
#                     if largest > 0:
#                         heappush(h, -largest)
#                 val -= 1
#                 if val <= 0 and not h:
#                     break
#                 if val > 0:
#                     heappush(h, -val)
#             return len(h) == 0 and val <= 0
            
            
#         lo, hi = 0, min(sum(usageLimits), (n * (n + 1)) // 2)
#         while lo < hi:
#             mid = (lo + hi + 1) // 2
#             if check(mid):
#                 lo = mid
#             else:
#                 hi = mid - 1
#         return lo

        usageLimits.sort()
        count = 0
        total = 0
        for i in range(n):
            total += usageLimits[i]
            nextReq = count + 1
            if total >= nextReq:
                total -= nextReq
                count += 1
        return count