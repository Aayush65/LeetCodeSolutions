class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        maxTime = 0
        for i in left:
            maxTime = max(maxTime, i)
        for i in right:
            maxTime = max(maxTime, n - i)
        return maxTime