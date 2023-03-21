class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        total = 0
        prevPrice = 0
        currLen = 0
        for i in prices:
            if not prevPrice or i == prevPrice - 1:
                currLen += 1
            else:
                currLen = 1
            total += currLen
            prevPrice = i
        return total
                