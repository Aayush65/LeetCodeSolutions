class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        indexMap = defaultdict(list)
        for i, x in enumerate(s):
            indexMap[x].append(i)
        
        maxDist = -1
        for i in indexMap:
            dist = indexMap[i][-1] - indexMap[i][0] - 1
            maxDist = max(maxDist, dist)
        return maxDist