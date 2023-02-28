class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        mod = 1000000007

        nodeMap = {i: [] for i in range(n)}
        for i, j, t in roads:
            nodeMap[i].append((j, t))
            nodeMap[j].append((i, t))

        q = [(0, 0)]
        timeMap = [float("inf")] * n
        ways = [0] * n
        ways[0] = 1
        while q:
            time, node = heappop(q)
            if node == n - 1:
                continue

            for i, t in nodeMap[node]:
                if time + t == timeMap[i]:
                    ways[i] += ways[node]
                elif time + t < timeMap[i]:
                    timeMap[i] = time + t
                    ways[i] = ways[node]
                    heappush(q, (time + t, i))

        return ways[-1] % mod