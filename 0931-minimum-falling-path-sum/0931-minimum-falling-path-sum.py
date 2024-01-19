class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        memo = {}

        def fall(i, j):
            if i == n - 1:
                return matrix[i][j]
            if (i, j) in memo:
                return memo[(i, j)]
            minSum = float("inf")
            if j > 0:
                minSum = min(fall(i + 1, j - 1), minSum)
            minSum = min(fall(i + 1, j), minSum)
            if j < n - 1:
                minSum = min(fall(i + 1, j + 1), minSum)
            minSum += matrix[i][j]
            memo[(i, j)] = minSum
            return minSum 

        minSum = float("inf")
        for i in range(n):
            minSum = min(fall(0, i), minSum)
        return minSum