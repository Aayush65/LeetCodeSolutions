class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:        
        color = [0 for _ in graph]
        for i in range(len(graph)):
            if color[i]:
                continue
            color[i] = 1
            q = deque([i])
            while q:
                node = q.popleft()
                for nei in graph[node]:
                    if color[nei] == color[node]:
                        return False
                    if color[nei] == 0:
                        color[nei] = color[node] * -1
                        q.append(nei)
        return True