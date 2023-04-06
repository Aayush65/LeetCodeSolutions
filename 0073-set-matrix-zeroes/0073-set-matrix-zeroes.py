class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        M = len(matrix)
        N = len(matrix[0])
        for i in range(M):
            isZeroFound = False
            for j in range(N):
                if matrix[i][j] == 0:
                    isZeroFound = True
                    for k in range(M):
                        if matrix[k][j]:
                            matrix[k][j] = 'A'
                            
            if isZeroFound:
                for k in range(N):
                    if matrix[i][k]:
                        matrix[i][k] = 'A'
                        
        for i in range(M):
            for j in range(N):
                if matrix[i][j] == 'A':
                    matrix[i][j] = 0