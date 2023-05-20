class UnionFind():
    def __init__(self, variables):
        self.root = {v: v for v in variables}
        self.rank = {v: 1 for v in variables}
        self.val = {v: 1 for v in variables}
        
    def find(self, x):
        if x not in self.root:
            return None, 0
        if x == self.root[x]:
            return x, self.val[x]
        self.root[x], m = self.find(self.root[x])
        self.val[x] *= m
        return self.root[x], self.val[x]
    
    def union(self, x, y, v):
        x, v_x = self.find(x)
        y, v_y = self.find(y)
        if x != y:
            if self.rank[x] < self.rank[y]:
                self.root[x] = y
                self.val[x] = v_y / v_x * v
            elif self.rank[y] < self.rank[x]:
                self.root[y] = x
                self.val[y] = v_x / v_y / v 
            else:
                self.root[y] = x
                self.rank[x] += 1
                self.val[y] = v_x / v_y / v
        
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        # Instantiate a UnionFind object
        variables = set()
        for e in equations:
            variables.add(e[0])
            variables.add(e[1])
        uf = UnionFind(variables)
        
        # Add relations
        for e, v in zip(equations, values):
            uf.union(e[0], e[1], v)
        
        # Calculate query outputs
        out = []
        for q in queries:
            r0, v0 = uf.find(q[0])
            r1, v1 = uf.find(q[1])
            if not r0 or not r1 or r0 != r1:
                out.append(-1)
            else:
                out.append(v0 / v1)
        return out