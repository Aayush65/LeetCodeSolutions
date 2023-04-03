class Solution:
    def findShortestCycle(self, n: int, edges: List[List[int]]) -> int:
        nodeMap = {i: set() for i in range(n)}
        for i, j in edges:
            nodeMap[i].add(j)
            nodeMap[j].add(i)
        
        minLen = float("inf")
        
        for i, j in edges:
            nodeMap[i].remove(j)
            nodeMap[j].remove(i)
            
            q = {i}
            steps = 1
            isLoop = False
            visited = set()
            while q:
                newQ = set()
                for node in q:
                    if node in visited:
                        continue
                    visited.add(node)
                    if node == j:
                        isLoop = True
                        minLen = min(steps, minLen)
                    for nextNodes in nodeMap[node]:
                        newQ.add(nextNodes)
                if isLoop:
                    break
                steps += 1
                q = newQ
            nodeMap[i].add(j)
            nodeMap[j].add(i)
            
        return -1 if minLen == float("inf") else minLen