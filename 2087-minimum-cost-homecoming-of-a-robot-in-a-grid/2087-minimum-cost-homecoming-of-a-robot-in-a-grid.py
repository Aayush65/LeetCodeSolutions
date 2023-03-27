class Solution:
    def minCost(self, startPos: List[int], homePos: List[int], rowCosts: List[int], colCosts: List[int]) -> int:
        ax, bx = min(startPos[0], homePos[0]), max(startPos[0], homePos[0]) 
        ay, by = min(startPos[1], homePos[1]), max(startPos[1], homePos[1]) 
        
        cost = 0
        for i in range(ax, bx + 1):
            cost += rowCosts[i]
        for i in range(ay, by + 1):
            cost += colCosts[i]
        return cost - rowCosts[startPos[0]] - colCosts[startPos[1]]
    