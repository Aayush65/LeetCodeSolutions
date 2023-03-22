class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = {}
        for i, j, k in roads:
            if i in graph:
                graph[i].add((j, k))
            else:
                graph[i] = {(j, k)}
            if j in graph:
                graph[j].add((i, k))
            else:
                graph[j] = {(i, k)}

        q = deque()
        for i in graph[1]:
            q.append([1, i[0], i[1]])
        minPath = float("inf")
        isVisited = n == 1
        visited = {1}
        while q:
            currNode, nextNode, dist = q.popleft()
            if nextNode == n:
                isVisited = True
            minPath = min(minPath, dist)
            if nextNode in visited:
                continue
            visited.add(nextNode)
            for nextNode, val in graph[nextNode]:
                q.append([nextNode, nextNode, val])
        return minPath if isVisited else -1
