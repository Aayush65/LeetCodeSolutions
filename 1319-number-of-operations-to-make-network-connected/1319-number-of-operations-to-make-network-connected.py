class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        par = [i for i in range(n)]
        rank = [0 for i in range(n)]
        
        def find(node: int) -> int:
            while node != par[node]:
                par[node] = par[par[node]]
                node = par[node]
            return node
        
        def union(node1: int, node2: int) -> bool:
            par1, par2 = find(node1), find(node2)
            if par1 == par2:
                rank[par1] += 1
                return False
            if rank[par1] >= rank[par2]:
                rank[par1] += 1 + rank[par2]
                rank[par2] = 0
                par[par2] = par1
            else:
                rank[par2] += 1 + rank[par1]
                rank[par1] = 0
                par[par1] = par2
            return True
        
        for i, j in connections:
            union(i, j)
        for i in range(n):
            par[i] = find(i)

        nodeMap = {i: 0 for i in par}
        for i in par:
            nodeMap[i] += 1
        numOfGroups = len(nodeMap)
        extraWires = 0
        for i in set(par):
            extraWires += rank[i] - nodeMap[i] + 1
        # print(par, rank, numOfGroups, extraWires)
        return numOfGroups - 1 if numOfGroups - 1 <= extraWires else -1