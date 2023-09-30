class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        currRow = [poured]
        
        currSum = poured
        while currSum:
            nextSum = 0
            nextRow = [0] * (len(currRow) + 1)
            if query_row == 0:
                return 1 if currRow[query_glass] >= 1 else currRow[query_glass]
            
            for i in range(len(currRow)):
                if currRow[i] <= 1:
                    continue
                overflow = currRow[i] - 1
                nextRow[i] += overflow / 2
                nextRow[i + 1] += overflow / 2
                nextSum += overflow
            currRow = nextRow
            currSum = nextSum
            query_row -= 1
        return 0        