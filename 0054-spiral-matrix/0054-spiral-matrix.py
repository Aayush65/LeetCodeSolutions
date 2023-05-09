class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        M = m = len(matrix)
        N = n = len(matrix[0])

        # right -> down -> left -> up
        # +j -> +i -> -j -> -i
        unspiraledMatrix = []
        direction = 1
        i, j = 0, 0
        while len(unspiraledMatrix) < M * N:
            count = 0
            while count < n:
                unspiraledMatrix.append(matrix[i][j])
                j += direction
                count += 1
            j -= direction
            n -= 1
            m -= 1
            count = 0
            while count < m:
                i += direction
                unspiraledMatrix.append(matrix[i][j])
                count += 1
            j -= direction
            direction *= -1
        return unspiraledMatrix
