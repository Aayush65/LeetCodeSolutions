class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascalTriangle = [[1]]
        for i in range(1, numRows):
            layer = []
            for j in range(i):
                prev = pascalTriangle[i-1][j-1] if j > 0 else 0
                layer.append(pascalTriangle[i-1][j] + prev)
            layer.append(1)
            pascalTriangle.append(layer)
        return pascalTriangle