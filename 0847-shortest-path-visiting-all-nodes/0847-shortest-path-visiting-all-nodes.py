class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        q = []
        n = len(graph)
        for i in range(n):
            mask = 1 << i 
            q.append((i, mask))
        
        steps = 0
        visited = set()
        while q:
            newQ = []
            for num, mask in q:
                if (num, mask) in visited:
                    continue
                visited.add((num, mask))
                if mask + 1 == 2 ** n:
                    return steps
                for nei in graph[num]:
                    newQ.append((nei, mask | (1 << nei)))
            q = newQ
            steps += 1