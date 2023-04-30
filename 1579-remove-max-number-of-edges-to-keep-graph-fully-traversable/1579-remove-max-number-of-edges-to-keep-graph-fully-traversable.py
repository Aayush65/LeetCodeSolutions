class UnionFind:

    def __init__(self, n: int):
        self.root = [i for i in range(n)]
        self.rank = [1 for _ in range(n)]
        self.group = n

    def find(self, x: int) -> int:
        if self.root[x] != x: self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x: int, y: int) -> None:
        root_x, root_y = self.find(x), self.find(y)
        if root_x == root_y: return
        if self.rank[root_x] > self.rank[root_y]: self.root[root_y] = root_x
        elif self.rank[root_x] < self.rank[root_y]: self.root[root_x] = root_y
        else:
            self.root[root_y] = root_x
            self.rank[root_x] += 1
        self.group -= 1

    def are_connected(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)


class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        uf_a, uf_b = UnionFind(n), UnionFind(n)
        res = 0
        edges.sort(reverse=True)
        for t, u, v in edges:
            if t == 3:
                if uf_a.are_connected(u - 1, v - 1) or uf_b.are_connected(u - 1,  v - 1): res += 1
                else:
                    uf_a.union(u - 1, v - 1)
                    uf_b.union(u - 1, v - 1)
            if t == 2:
                if uf_a.are_connected(u - 1, v - 1): res += 1
                else: uf_a.union(u - 1, v - 1)
            if t == 1:
                if uf_b.are_connected(u - 1, v - 1): res += 1
                else: uf_b.union(u - 1, v - 1)
            
        return res if uf_a.group == uf_b.group == 1 else -1