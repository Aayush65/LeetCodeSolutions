class Solution:
    def numberOfSets(self, n: int, maxDistance: int, roads: List[List[int]]) -> int:
    
        def shortestPairs(roads: list[list[int]]):
            shortestDist = [[0 if i == j else float("inf") for i in range(n)] for j in range(n)]
            for i, j, w in roads:
                shortestDist[i][j] = min(shortestDist[i][j], w)
                shortestDist[j][i] = min(shortestDist[j][i], w)

            for k in range(n):
                for i in range(n):
                    for j in range(n):
                        shortestDist[i][j] = min(shortestDist[i][j], shortestDist[i][k] + shortestDist[k][j])
            # print(shortestDist)
            return shortestDist

        def check(mask: int) -> bool:
            allowed = []
            for i, j, w in roads:
                if (mask >> i) & 1 and (mask >> j) & 1:
                    allowed.append((i, j, w))
            pairs = shortestPairs(allowed)
            maxShortestDist = 0
            for i in range(n):
                for j in range(n):
                    if (mask >> i) & 1 and (mask >> j) & 1 and pairs[i][j] == float("inf"):
                        return False
                    if pairs[i][j] == float("inf"):
                        continue
                    maxShortestDist = max(maxShortestDist, pairs[i][j])
            return maxShortestDist <= maxDistance

        count = 0
        for i in range(2 ** n):
            if check(i):
                # print(bin(i)[2:].zfill(n))
                count += 1
        return count