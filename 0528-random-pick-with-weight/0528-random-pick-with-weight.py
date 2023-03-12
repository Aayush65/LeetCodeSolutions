class Solution:

    def __init__(self, w: List[int]):
        self.preSum = []
        self.total = 0
        for i in w:
            self.total += i
            self.preSum.append(self.total)

    def pickIndex(self) -> int:
        rand = randint(1, self.total)
        index = bisect_left(self.preSum, rand)
        return index
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()