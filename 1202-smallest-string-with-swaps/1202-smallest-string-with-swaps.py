class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        
        def find(n: int) -> int:
            while n != par[n]:
                par[n] = par[par[n]]
                n = par[n]
            return n
        
        def union(n1: int, n2: int) -> bool:
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return False
            if rank[p1] >= rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
                rank[p2] = 0
            else:
                par[p1] = p2
                rank[p2] += rank[p1]
                rank[p1] = 0
            return True
        
        n = len(s)
        newS = list(s)
        par = [i for i in range(n)]
        rank = [1] * n
        
        for i, j in pairs:
            union(i, j)
        
        family = {}
        for i in range(n):
            root = find(i)
            if root not in family:
                family[root] = []
            family[root].append(i)
            
        for root in family:
            chars = sorted([s[i] for i in family[root]])
            for i, ch in zip(family[root], chars):
                newS[i] = ch             
            
        return ''.join(newS)