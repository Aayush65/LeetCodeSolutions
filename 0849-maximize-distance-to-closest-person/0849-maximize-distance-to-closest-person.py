class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        res = 1
        empty = 0
        for i in range(len(seats)):
            if seats[i] == 0:
                empty += 1
                if i == empty - 1 or i == len(seats) - 1:
                    res = max(res, empty)
                res = max(res, (empty + 1) // 2)
            else:
                empty = 0
        
        return res