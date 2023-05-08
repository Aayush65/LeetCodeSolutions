class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m = len(mat)
        n = len(mat[0])
        res = []
        for i in range(m + n - 1):
            diag = []
            for j in range(i + 1):
                if j < m and i - j < n:
                    diag.append(mat[j][i - j])
            if i % 2 == 0:
                diag.reverse()
            for j in diag:
                res.append(j)
        return res