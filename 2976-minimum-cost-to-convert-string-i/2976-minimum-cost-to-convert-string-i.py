class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        indexOf = lambda x: ord(x) - ord('a')
        movementChart = [[float("inf")] * 26 for _ in range(26)]
        for i in range(26):
            movementChart[i][i] = 0
        for i, j, val in zip(original, changed, cost):
            i, j = indexOf(i), indexOf(j)
            movementChart[i][j] = min(movementChart[i][j], val)
        
        for k in range(26):
            for i in range(26):
                for j in range(26):
                    movementChart[i][j] = min(movementChart[i][j], movementChart[i][k] + movementChart[k][j])
        
        totalCost = 0
        for i, j in zip(source, target):
            i, j = indexOf(i), indexOf(j)
            totalCost += movementChart[i][j]
        return -1 if totalCost == float("inf") else totalCost