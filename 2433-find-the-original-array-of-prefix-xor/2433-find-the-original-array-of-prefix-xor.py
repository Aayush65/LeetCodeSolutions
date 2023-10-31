class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        currXor = 0
        res = []
        for i in pref:
            res.append(currXor ^ i)
            currXor ^= res[-1]
        return res