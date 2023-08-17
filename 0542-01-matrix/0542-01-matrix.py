class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        q = set()
        for i in range(m):
            for j in range(n):
                if not mat[i][j]:
                    q.add((i, j))

        dist = 0
        res = [[0]*n for i in range(m)]
        visited = set()
        while q:
            newQ = set()
            for i, j in q:
                if (i, j) in visited:
                    continue
                visited.add((i, j))
                if mat[i][j]:
                    res[i][j] = dist
                
                if i > 0:
                    newQ.add((i - 1, j))
                if j > 0:
                    newQ.add((i, j - 1))
                if i < m - 1:
                    newQ.add((i + 1, j))
                if j < n - 1:
                    newQ.add((i, j + 1))
            dist += 1
            q = newQ
        return res              