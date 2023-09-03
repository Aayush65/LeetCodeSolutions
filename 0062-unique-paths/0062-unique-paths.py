class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        paths = [[0 for x in range(n)] for y in range(m)]
        paths[0][0] = 1
        for i in range(m):
            for j in range(n):
                if not i and not j:
                    continue
                if not i:
                    paths[i][j] = paths[i][j-1]
                elif not j:
                    paths[i][j] = paths[i-1][j]
                else:
                    paths[i][j] = paths[i][j-1] +  paths[i-1][j]
        return paths[-1][-1]