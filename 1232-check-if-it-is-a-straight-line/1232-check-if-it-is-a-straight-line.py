class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        x1, y1 = coordinates[0]
        slopes = set()
        
        for i in range(1, len(coordinates)):
            x2, y2 = coordinates[i]
            slopes.add((y2 - y1) / (x2 - x1) if x2 != x1 else float("inf"))
            if len(slopes) > 1:
                return False
        return True