class FrequencyTracker:

    def __init__(self):
        self.hm = defaultdict(int)
        self.freqMap = defaultdict(int)

    def add(self, number: int) -> None:
        if self.hm[number]:
            self.freqMap[self.hm[number]] -= 1
        self.hm[number] += 1
        self.freqMap[self.hm[number]] += 1

    def deleteOne(self, number: int) -> None:
        if self.hm[number]:
            self.freqMap[self.hm[number]] -= 1
            self.hm[number] -= 1
            if self.hm[number]:
                self.freqMap[self.hm[number]] += 1

    def hasFrequency(self, frequency: int) -> bool:
        return self.freqMap[frequency] != 0


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)

# [null,null,null,null,false,false,false]