class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1]
        denominator = 1
        numerator = 1
        for i in range(rowIndex):
            numerator *= (rowIndex - i)
            denominator *= i + 1
            row.append(numerator//denominator)
        return row