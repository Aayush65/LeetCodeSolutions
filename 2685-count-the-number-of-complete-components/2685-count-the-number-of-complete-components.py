class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        par = [i for i in range(n)]
        rank = [1] * n
        edge = [0] * n
        
        def find(n: int) -> int:
            while n != par[n]:
                par[n] = par[par[n]]
                n = par[n]
            return n
        
        def union(n1: int, n2: int) -> bool:
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                edge[p1] += 1
                return False
            if rank[p1] >= rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
                rank[p2] = 0
                edge[p1] += 1 + edge[p2]
                edge[p2] = 0
            else:
                par[p1] = p2
                rank[p2] += rank[p1]
                rank[p1] = 0
                edge[p2] += 1 + edge[p1]
                edge[p1] = 0
            return True
        
        for i, j in edges:
            union(i, j)
        
        @cache
        def c(n: int, r: int) -> int:
            if n < r:
                return 0
            numerator = 1
            denominator = 1
            r = min(n, n - r)
            for i in range(r):
                numerator *= n
                denominator *= i + 1
                n -= 1
            return numerator // denominator
        
        completeComp = 0
        for i in range(n):
            if not rank[i]:
                continue
            noOfVertices = rank[i]
            noOfEdges = edge[i]
            # print(noOfVertices, noOfEdges, c(noOfVertices, 2))
            if noOfEdges == c(noOfVertices, 2):
                completeComp += 1
        return completeComp
            
            