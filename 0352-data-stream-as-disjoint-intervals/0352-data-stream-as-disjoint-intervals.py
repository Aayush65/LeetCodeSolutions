class SummaryRanges:

    def __init__(self):
        self.allNums = set()

    def addNum(self, value: int) -> None:
        self.allNums.add(value)

    def getIntervals(self) -> List[List[int]]:
        nums = sorted(list(self.allNums))
        intervals = []
        i = 0
        while i < len(nums):
            nextInterval = [nums[i]]
            j = nums[i]
            while j in self.allNums:
                j += 1
                i += 1
            nextInterval.append(j - 1)
            intervals.append(nextInterval)
        return intervals
            


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()