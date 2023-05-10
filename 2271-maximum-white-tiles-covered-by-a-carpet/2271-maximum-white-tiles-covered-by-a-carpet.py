class Solution:
    def maximumWhiteTiles(self, tiles: List[List[int]], carpetLen: int) -> int:
        tiles.sort()
        preSum = [0]
        for i, j in tiles:
            preSum.append(preSum[-1] + j - i + 1)
        
        def search(start: int, val: int) -> list[int]:
            i = start
            j = len(tiles) - 1
            while i <= j:
                if val >= tiles[j][1]:
                    return [j, tiles[j][1] - tiles[j][0]]
                if val < tiles[i][0]:
                    return [i - 1, tiles[i - 1][1] - tiles[i - 1][0]]
                mid = (i + j) // 2
                if tiles[mid][0] > val:
                    j = mid - 1
                elif tiles[mid][1] < val:
                    i = mid + 1
                else:
                    return [mid, val - tiles[mid][0]]
        
        carpetLen -= 1
        maxCovered = 0
        for i in range(len(tiles)):
            endIndex, tileNo = search(i, tiles[i][0] + carpetLen)
            covered = preSum[endIndex] - preSum[i] + tileNo + 1
            maxCovered = max(maxCovered, covered)
        return maxCovered