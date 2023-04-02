class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        freqMap = {i: 0 for i in nums}
        for i in nums:
            freqMap[i] += 1
            
        res = []
        while freqMap:
            row = []
            for i in freqMap:
                row.append(i)
            for i in row:
                freqMap[i] -= 1
                if freqMap[i] == 0:
                    del freqMap[i]
            res.append(row)
        return res