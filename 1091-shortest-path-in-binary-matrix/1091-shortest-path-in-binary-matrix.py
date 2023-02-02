class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if n == 1:
            if not grid[0][0]:
                return 1
        dist = 0
        visited = set()
        isValid = lambda x, y: -1 < x < n and -1 < y < n and not grid[x][y]
        q = []
        if not grid[0][0]: 
            q.append([0,0])
        
        while q:
            newQ = []
            dist += 1
            for i, j in q:
                if (i, j) in visited:
                    continue
                visited.add((i, j))
                for x, y in [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]:
                    if isValid(i + x, j + y):
                        if (i + x, j + y) == (n - 1, n - 1):
                            return dist + 1
                        newQ.append([i + x, j + y])
            q = newQ
        return -1
        