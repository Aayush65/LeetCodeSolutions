class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        count = 0
        
        # x1 <= x2
        # y1 >= y2
        
        
        for p1 in points:
            x1, y1 = p1
            for p2 in points:
                x2, y2 = p2
                if p1 == p2 or x1 > x2 or y1 < y2:
                    continue
                boxEmpty = True
                for p3 in points:
                    if p3 == p1 or p3 == p2:
                        continue
                    x3, y3 = p3
                    if x1 <= x3 <= x2 and y2 <= y3 <= y1:
                        boxEmpty = False
                        break
                if boxEmpty:
                    count += 1
                    
        return count