class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        same = 0
        
        possibles = {tops[0], bottoms[0]}
        for i, j in zip(tops, bottoms):
            if i not in possibles and j not in possibles:
                return -1
            if i in possibles and j in possibles:
                possibles = {i, j}
            elif i in possibles:
                possibles = {i}
            else:
                possibles = {j}            
            if i == j:
                same += 1
                
        def noOfFlips(arr: list[int], target: int) -> int:
            flips = 0
            for i in arr:
                if i != target:
                    flips += 1
            return flips
            
        p1 = possibles.pop()
        if len(possibles) == 2:
            p2 = possibles.pop()
            return min(noOfFlips(tops, p1), noOfFlips(tops, p2), noOfFlips(bottoms, p1), noOfFlips(bottoms, p2))
        return min(noOfFlips(tops, p1), noOfFlips(bottoms, p1))
        
            
            