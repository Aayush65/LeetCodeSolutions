class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        nodeMap = {i: [] for i in range(n)}
        for i, j in edges:
            nodeMap[i].append(j)
            nodeMap[j].append(i)
        restricted = set(restricted)

        visited = set()
        q = deque([0])
        while q:
            node = q.popleft()
            if node in visited:
                continue
            visited.add(node)
            for i in nodeMap[node]:
                if i in restricted:
                    continue
                q.append(i)
        return len(visited)