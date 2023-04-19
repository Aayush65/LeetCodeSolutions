class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        nodeMap = {i: [] for i in range(n)}
        for i, j in connections:
            nodeMap[i].append((j, True))
            nodeMap[j].append((i, False))
            
        q = deque([0])
        toReverse = 0
        visited = {0}
        while q:
            city = q.popleft()
            for nei, isForward in nodeMap[city]:
                if nei in visited:
                    continue
                visited.add(nei)
                q.append(nei)
                if isForward:
                    toReverse += 1
        return toReverse
        