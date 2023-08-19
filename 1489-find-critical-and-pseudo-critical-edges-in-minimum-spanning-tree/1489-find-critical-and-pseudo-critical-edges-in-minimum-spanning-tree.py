class UnionFind:
    def __init__(self, n: int):
        self.par = [i for i in range(n)]
        self.rank = [1] * n
        
    def find(self, n: int) -> int:
        while n != self.par[n]:
            self.par[n] = self.par[self.par[n]]
            n = self.par[n]
        return n

    def union(self, n1: int, n2: int) -> bool:
        p1, p2 = self.find(n1), self.find(n2)
        if p1 == p2:
            return False
        if self.rank[p1] >= self.rank[p2]:
            self.par[p2] = p1
            self.rank[p1] += self.rank[p2]
        else:
            self.par[p1] = p2
            self.rank[p2] += self.rank[p1]
        return True
        

class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        for i, edge in enumerate(edges):
            edge.append(i)
        edges.sort(key = lambda x: x[2])
        
        min_weight = 0
        ut = UnionFind(n)
        for v1, v2, w, idx in edges:
            if ut.union(v1, v2):
                min_weight += w
        
        
        critical, pseudo = [], []
        
        for i1, j1, w1, idx1 in edges:
            weight = 0
            uf = UnionFind(n)
            for i2, j2, w2, idx2 in edges:
                if idx1 != idx2 and uf.union(i2, j2):
                    weight += w2
            if weight != min_weight or max(uf.rank) != n:
                critical.append(idx1)
                continue
            
            weight = w1
            uf = UnionFind(n)
            uf.union(i1, j1)
            for i2, j2, w2, idx2 in edges:
                if uf.union(i2, j2):
                    weight += w2
            if weight == min_weight and max(uf.rank) == n:
                pseudo.append(idx1)
                
        return [critical, pseudo]