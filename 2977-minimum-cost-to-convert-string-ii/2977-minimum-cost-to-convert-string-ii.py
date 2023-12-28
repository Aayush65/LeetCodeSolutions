class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        allPoints = {x: i for i, x in enumerate(list(set(original + changed)))}
        n = len(allPoints)
        dist = [[float("inf")] * n for _ in range(n)]
        for i in range(n):
            dist[i][i] = 0

        for i, j, val in zip(original, changed, cost):
            i, j = allPoints[i], allPoints[j]
            dist[i][j] = min(dist[i][j], val)

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
                    
        allLens = sorted(list({len(i) for i in allPoints}))
        n = len(source)
        
        @cache
        def dp(index: int) -> int:
            if index == n:
                return 0
            res = float("inf")
            if source[index] == target[index]:
                res = dp(index + 1)
            for i in allLens:
                if index + i > n:
                    break
                srcSubStr = source[index: index + i]
                trgSubStr = target[index: index + i]
                if srcSubStr in allPoints and trgSubStr in allPoints:
                    cost = dist[allPoints[srcSubStr]][allPoints[trgSubStr]]
                    if cost != float("inf"):
                        res = min(res, cost + dp(index + i))
            return res

        res = dp(0)
        return -1 if res == float("inf") else res