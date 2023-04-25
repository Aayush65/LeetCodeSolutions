class SmallestInfiniteSet:

    def __init__(self):
        self.infiniteSet = [i for i in range(1, 1001)]
        self.notInInfiniteSet = set()

    def popSmallest(self) -> int:
        poped = heappop(self.infiniteSet)
        self.notInInfiniteSet.add(poped)
        return poped

    def addBack(self, num: int) -> None:
        if num in self.notInInfiniteSet:
            heappush(self.infiniteSet, num)
            self.notInInfiniteSet.remove(num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)