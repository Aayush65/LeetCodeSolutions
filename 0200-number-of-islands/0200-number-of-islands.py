class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        parent = [i for i in range(m * n)]
        rank = [int(grid[i][j]) for i in range(m) for j in range(n)]

        def find(node: int) -> int:
            while node != parent[node]:
                parent[node] = parent[parent[node]]
                node = parent[node]
            return node

        def union(node1: int, node2: int) -> bool:
            par1, par2 = find(node1), find(node2)
            if par1 == par2:
                return False
            if rank[par1] >= rank[par2]:
                parent[par2] = par1
                rank[par1] += rank[par2]
                rank[par2] = 0
            else:
                parent[par1] = par2
                rank[par2] += rank[par1]
                rank[par1] = 0
            return True


        for i in range(m):
            for j in range(n):
                index = i * n + j
                if grid[i][j] == '1':
                    if i != m - 1 and grid[i + 1][j] == '1':
                        union(index, index + n)
                    if j != n - 1 and grid[i][j + 1] == '1':
                        union(index, index + 1)

        # print(rank)
        # print(parent)
        islands = 0
        for i in rank:
            if i:
                islands += 1
        return islands