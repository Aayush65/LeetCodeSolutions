class Solution:
    def countPairs(self, coordinates: List[List[int]], k: int) -> int:
        hm = {tuple(i): 0 for i in coordinates}
        for i in coordinates:
            hm[tuple(i)] += 1
    
        count = 0
        coordinates = list(set([(i, j) for i, j in coordinates]))
        for x, y in coordinates:
            for i in range(k + 1):
                j = k - i
                x2 = x ^ i
                y2 = y ^ j
                if (x, y) == (x2, y2):
                    count += (hm[(x, y)] * (hm[(x, y)] - 1)) // 2
                elif (x2, y2) in hm:
                    count += hm[(x, y)] * hm[(x2, y2)]
            del hm[(x, y)]
            
        return count
        