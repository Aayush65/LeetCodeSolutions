class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        total = 0
        for i in range(len(mat)):
            total += mat[i][i]
            if i + 1 != len(mat) - i:
                total += mat[i][len(mat) - i - 1]
        return total