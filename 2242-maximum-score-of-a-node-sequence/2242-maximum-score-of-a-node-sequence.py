class Solution:
    def maximumScore(self, scores: List[int], edges: List[List[int]]) -> int:
        n = len(scores)
        nodeMap = {i: [] for i in range(n)}
        for i, j in edges:
            heappush(nodeMap[i], (scores[j], j))
            if len(nodeMap[i]) > 3:
                heappop(nodeMap[i])
            heappush(nodeMap[j], (scores[i], i))
            if len(nodeMap[j]) > 3:
                heappop(nodeMap[j])
        
        maxScore = -1
        for i, j in edges:
            for s1, n1 in nodeMap[i]:
                if n1 == j:
                    continue
                for s2, n2 in nodeMap[j]:
                    if n2 == n1 or n2 == i:
                        continue
                    maxScore = max(maxScore, s1 + scores[i] + scores[j] + s2)
        return maxScore