class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        N = n

        # right -> down -> left -> up
        # +j -> +i -> -j -> -i
        matrix = [[-1]*n for _ in range(n)]
        direction = 1
        i, j = 0, 0
        currNumber = 1
        while currNumber <= N ** 2:
            count = 0
            while count < n:
                matrix[i][j] = currNumber
                currNumber += 1
                j += direction
                count += 1
            j -= direction
            n -= 1
            count = 0
            while count < n:
                i += direction
                matrix[i][j] = currNumber
                currNumber += 1
                count += 1
            j -= direction
            direction *= -1
        return matrix