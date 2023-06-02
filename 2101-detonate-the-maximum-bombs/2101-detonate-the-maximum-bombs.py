class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        # Union find will not work because:
        # Union find only works on non directed graphs, but doesn't work on directed graphs

        n = len(bombs)
        dist = lambda c1, c2: (c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2 

        memo = {}
        def dfs(index: int) -> int:
            if (index, tuple(visited)) in memo:
                return memo[(index, tuple(visited))]
            x1, y1, r1 = bombs[index]
            visited[index] = 1
            blastZone = 1
            for i in range(n):
                x2, y2, r2 = bombs[i]
                if visited[i]:
                    continue
                if dist((x1, y1), (x2, y2)) <= r1 ** 2:
                    blastZone += dfs(i)
            memo[(index, tuple(visited))] = blastZone
            return blastZone

        maxBlastZone = 1
        for i in range(n):
            visited = [0] * n
            maxBlastZone = max(maxBlastZone, dfs(i))
        return maxBlastZone
