class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        redMap = {i: [] for i in range(n)}
        for i, j in redEdges:
            redMap[i].append(j)

        blueMap = {i: [] for i in range(n)}
        for i, j in blueEdges:
            blueMap[i].append(j)
        
        res = [-1] * n
        q = {(0, 0), (0, 1)}
        visited = set()
        dist = 0
        while q:
            newQ = set()
            for i, isRed in q:
                if (i, isRed) in visited:
                    continue
                visited.add((i, isRed))
                if res[i] == -1:
                    res[i] = dist
                if isRed:
                    for j in blueMap[i]:
                        newQ.add((j, 0))
                else:
                    for j in redMap[i]:
                        newQ.add((j, 1))
            q = newQ
            dist += 1
        
        return res