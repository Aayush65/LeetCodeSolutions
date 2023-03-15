class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        par = [i for i in range(n)]
        rank = [1 for i in range(n)]

        def find(node: int) -> int:
            while node != par[node]:
                par[node] = par[par[node]]
                node = par[node]
            return node
        
        def union(node1: int, node2: int) -> bool:
            p1, p2 = find(node1), find(node2)
            if p1 == p2:
                return False
            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
                rank[p2] = 0
            else:
                par[p1] = p2
                rank[p2] += rank[p1]
                rank[p1] = 0
            return True
        
        for i, j in edges:
            union(i, j)
        sizes = []
        for i in rank:
            if i:
                sizes.append(i)
        
        count = 0
        for i in sizes:
            count += i * (n - i)
        return count // 2
