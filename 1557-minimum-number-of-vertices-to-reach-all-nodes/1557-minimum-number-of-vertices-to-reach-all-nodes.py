class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        par = [i for i in range(n)]
        
        def find(n: int) -> int:
            while n != par[n]:
                par[n] = par[par[n]]
                n = par[n]
            return n
        
        def union(n1: int, n2: int) -> None:
            p1, p2 = find(n1), find(n2)
            if p2 != n2:
                return
            par[p2] = p1
        
        for i, j in edges:
            union(i, j)
        
        res = set()
        for i in range(n):
            res.add(find(i))
        return res