class NumberContainers:

    def __init__(self):
        self.indexMap = {}
        self.numMap = {}

    def change(self, index: int, number: int) -> None:
        self.indexMap[index] = number
        if number not in self.numMap:
            self.numMap[number] = []
        heappush(self.numMap[number], index)

    def find(self, number: int) -> int:
        if number not in self.numMap:
            return -1
        while self.numMap[number] and self.indexMap[self.numMap[number][0]] != number:
            heappop(self.numMap[number])
        return self.numMap[number][0] if self.numMap[number] else -1


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)