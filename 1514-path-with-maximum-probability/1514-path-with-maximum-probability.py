class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        nodeMap = {i: [] for i in range(n)}
        succProb = [-log10(i) for i in succProb]
        for i in range(len(edges)):
            nodeMap[edges[i][0]].append([edges[i][1], succProb[i]])
            nodeMap[edges[i][1]].append([edges[i][0], succProb[i]])
        

        q = [(0, start)]
        probMap = {i: float('inf') for i in range(n)}
        probMap[start] = 0
        maxProb = float("inf")
        while q:
            prob, node = heappop(q)
            if node == end:
                maxProb = min(maxProb, prob)
                continue

            for i, p in nodeMap[node]:
                if probMap[i] > prob + p:
                    heappush(q, (prob + p, i))
                    probMap[i] = p + prob
        maxProb *= -1
        return 10 ** maxProb