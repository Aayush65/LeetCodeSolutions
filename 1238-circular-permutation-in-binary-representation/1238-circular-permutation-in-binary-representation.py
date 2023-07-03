class Solution:
    def circularPermutation(self, n: int, start: int) -> List[int]:
        grayCode = []
        currNum = 0
        visited = set()
        
        j = 0
        for i in range(2 ** n):
            if currNum == start:
                j = len(grayCode)
            grayCode.append(currNum)
            visited.add(currNum)
            MSBIndex = 0
            nextNum = currNum ^ (2 ** MSBIndex)
            while nextNum in visited:
                MSBIndex += 1
                nextNum = currNum ^ (2 ** MSBIndex)
            currNum = nextNum
        
        res = []
        currIdx = j
        for i in range(2 ** n):
            res.append(grayCode[j % (2 ** n)])
            j += 1
        return res
            