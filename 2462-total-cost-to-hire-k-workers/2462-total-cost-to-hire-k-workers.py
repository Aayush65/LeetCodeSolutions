class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        hStart, hEnd = [], []
        n = len(costs)
        i, j = 0, n - 1
        for i in range(candidates):
            heappush(hStart, costs[i])

        for j in range(candidates):
            if n - j == i + 1:
                break
            heappush(hEnd, costs[n - j - 1])
        j = n - candidates

        totalCost = 0
        for _ in range(k):
            if hStart and (not hEnd or hStart[0] <= hEnd[0]):
                totalCost += heappop(hStart)
                i += 1
                if i < j:
                    heappush(hStart, costs[i])
            else:
                totalCost += heappop(hEnd)
                j -= 1
                if i < j:
                    heappush(hEnd, costs[j])
        return totalCost