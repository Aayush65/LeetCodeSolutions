class UnionFind:
    def __init__(self, arr):
        self.arr = arr
        self.nodes = set()
        for i, j in arr:
            self.nodes.add(i)
            self.nodes.add(j)
        self.parent = {i: i for i in self.nodes}
        self.rank = {i: 1 for i in self.nodes}

    def find(self, node: int) -> int:
        while node != self.parent[node]:
            self.parent[node] = self.parent[self.parent[node]]
            node = self.parent[node]
        return node

    def union(self, node1: int, node2: int) -> int:
        par1, par2 = self.find(node1), self.find(node2)
        if par1 == par2:
            return 0
        if self.rank[par1] >= self.rank[par2]:
            self.parent[par2] = par1
            self.rank[par1] += self.rank[par2]
        else:
            self.parent[par1] = par2
            self.rank[par2] += self.rank[par1]
        return 1

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        arr = []
        for i in range(n):
            for j in range(n):
                if isConnected[i][j]:
                    arr.append([-(i + 1), j + 1])
        
        ut = UnionFind(arr)
        res = len(ut.nodes)
        for i, j in arr:
            res -= ut.union(ut.find(i), ut.find(j))
        return res