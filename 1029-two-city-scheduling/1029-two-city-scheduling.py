class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key = lambda x: x[1] - x[0])
        n = len(costs) // 2
        cost = 0
        for i in range(n):
            cost += costs[i][1]
        for i in range(n, n * 2):
            cost += costs[i][0]
        return cost        