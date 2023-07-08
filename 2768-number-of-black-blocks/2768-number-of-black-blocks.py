class Solution:
    def countBlackBlocks(self, m: int, n: int, coordinates: List[List[int]]) -> List[int]:
        blockMap = {}
        
        isValid = lambda x, y: -1 < x < m - 1 and -1 < y < n - 1
        
        for i, j in coordinates:
            if isValid(i - 1, j - 1):
                if (i - 1, j - 1) not in blockMap:
                    blockMap[(i - 1, j - 1)] = 0
                blockMap[(i - 1, j - 1)] += 1
            
            if isValid(i, j - 1):
                if (i, j - 1) not in blockMap:
                    blockMap[(i, j - 1)] = 0
                blockMap[(i, j - 1)] += 1
            
            if isValid(i - 1, j):
                if (i - 1, j) not in blockMap:
                    blockMap[(i - 1, j)] = 0
                blockMap[(i - 1, j)] += 1
        
            if isValid(i, j):
                if (i, j) not in blockMap:
                    blockMap[(i, j)] = 0
                blockMap[(i, j)] += 1
            
        res = [0] * 5
        for i in blockMap:
            res[blockMap[i]] += 1
        res[0] = (m - 1) * (n - 1) - sum(res)            
        return res
        