class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        maxLen = 0
        loopsLen = [-1] * len(edges)
        for i in range(len(edges)):
            if loopsLen[i] != -1:
                continue
            length = 0
            tempI = i
            visited = set()
            while tempI > -1 and loopsLen[tempI] == -1 and tempI not in visited:
                visited.add(tempI)
                loopsLen[tempI] = length
                tempI = edges[tempI]
                length += 1
            if tempI != -1 and tempI in visited:
                maxLen = max(maxLen, length - loopsLen[tempI])
        return maxLen if maxLen else -1