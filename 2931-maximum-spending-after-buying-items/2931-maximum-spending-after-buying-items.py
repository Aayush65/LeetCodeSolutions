class Solution:
    def maxSpending(self, values: List[List[int]]) -> int:
#         h = []
#         for i in range(len(values)):
#             heappush(h, values[i][-1])
        
#         spent = 0
#         day = 1
#         while h:
#             bought = heappop(h)
#             spent += bought * day
#             for i in range(len(values)):
#                 if values[i] and values[i][-1] == bought:
#                     values[i].pop()
#                     if values[i]:
#                         heappush(h, values[i][-1])
#             day += 1
#         return spent
        h = sorted([j for i in values for j in i])
        return sum((i + 1) * h[i] for i in range(len(h)))