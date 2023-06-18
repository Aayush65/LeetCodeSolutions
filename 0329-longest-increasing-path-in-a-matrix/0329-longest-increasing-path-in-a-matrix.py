class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        
        isValid = lambda x, y: -1 < x < m and -1 < y < n
        
        @cache
        def dfs(i: int, j: int) -> int:
            path = 1
            for x, y in [(i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1)]:
                if isValid(x, y) and matrix[x][y] > matrix[i][j]:
                    path = max(path, 1 + dfs(x, y))
            return path
            
        longestPath = 1
        for i in range(m):
            for j in range(n):
                longestPath = max(longestPath, dfs(i, j))
        return longestPath