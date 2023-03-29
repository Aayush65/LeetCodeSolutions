class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        minMax = float("inf")
        count = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] < 0:
                    count += 1
                    matrix[i][j] *= -1
                minMax = min(minMax, abs(matrix[i][j]))                
        
        total = 0
        for i in matrix:
            for j in i:
                total += j
        if count % 2:
            total -= 2 * minMax
        return total