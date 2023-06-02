class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        # Union find will not work because:
        # Union find only works on non directed graphs, but doesn't work on directed graphs

        n = len(bombs)
        dist = lambda c1, c2: (c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2

        nodeMap = {i: [] for i in range(n)}
        for i in range(n):
            for j in range(n):
                if i == j: continue
                if dist(bombs[i][:2], bombs[j][:2]) <= bombs[i][2] ** 2:
                    nodeMap[i].append(j)

        memo = {}
        def dfs(node: int) -> int:
            if (node, tuple(visited)) in memo:
                return memo[(node, tuple(visited))]
            visited[node] = 1
            blastZone = 1
            for nei in nodeMap[node]:
                if visited[nei]: continue
                blastZone += dfs(nei)
            return blastZone

        maxBlastZone = 1
        for i in range(n):
            visited = [0] * n
            maxBlastZone = max(maxBlastZone, dfs(i))
        return maxBlastZone