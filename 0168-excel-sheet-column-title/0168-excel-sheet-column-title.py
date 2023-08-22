class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = []
        while columnNumber:
            columnNumber -= 1
            nextAlphaNo = columnNumber % 26
            nextAlpha = chr(ord('A') + nextAlphaNo)
            res.append(nextAlpha)
            columnNumber //= 26            
        return ''.join(res[::-1])