class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        nodeMap = {i: set() for i in range(n)}
        for i, j in roads:
            nodeMap[i].add(j)
            nodeMap[j].add(i)
            
        maxNetRank = 0
        for i in range(n):
            for j in range(i + 1, n):
                netRank = len(nodeMap[i]) + len(nodeMap[j])
                if j in nodeMap[i]:
                    netRank -= 1                
                maxNetRank = max(maxNetRank, netRank)
        return maxNetRank