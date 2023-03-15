class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        n = len(edges)
        
        scores = [0] * n
        maxScore = 0
        maxIndex = 0
        for i in range(n):
            scores[edges[i]] += i
            if scores[edges[i]] > maxScore:
                maxScore = scores[edges[i]]
                maxIndex = edges[i]
            elif scores[edges[i]] == maxScore:
                maxIndex = min(maxIndex, edges[i])
        return maxIndex
        