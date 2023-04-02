class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        par = [i for i in range(26)]
        rank = [0 for i in range(26)]
        indexOf = lambda x: ord(x) - ord('a')
        
        def find(n: int) -> int:
            while n != par[n]:
                n = par[n]
            return n
        
        def union(n1: int, n2: int) -> bool:
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return False
            if rank[p1] >= rank[p2]:
                rank[p1] += rank[p2]
                rank[p2] = 0
                par[p2] = p1
            else:
                rank[p2] += rank[p1]
                rank[p1] = 0
                par[p1] = p2
            return True
        
        for eq in equations:
            a, b = eq[0], eq[-1]
            isEqual = eq[1] == '='
            if isEqual:
                union(indexOf(a), indexOf(b))
            
        for eq in equations:
            a, b = eq[0], eq[-1]
            isEqual = eq[1] == '='
            if not isEqual:
                if find(indexOf(a)) == find(indexOf(b)):
                    return False
        return True