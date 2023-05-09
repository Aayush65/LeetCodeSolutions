class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        vals = []
        for i in grid:
            for j in i:
                vals.append(j)
        vals.sort()
        
        def calcMoves(val: int) -> int:
            moves = 0
            for i in vals:
                if abs(val - i) % x:
                    return -1
                moves += abs(val - i) // x
            return moves
        
        if len(vals) % 2:
            median = vals[len(vals) // 2]
            return calcMoves(median)
        else:
            median1 = vals[len(vals) // 2]
            median2 = vals[len(vals) // 2 - 1]
            return min(calcMoves(median1), calcMoves(median2))
            