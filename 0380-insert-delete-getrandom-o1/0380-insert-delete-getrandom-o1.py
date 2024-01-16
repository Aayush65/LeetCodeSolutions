class RandomizedSet:

    def __init__(self):
        self.arr = []
        self.indexMap = {}

    def insert(self, val: int) -> bool:
        if val not in self.indexMap:
            self.indexMap[val] = len(self.arr)
            self.arr.append(val)
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if val in self.indexMap:
            self.indexMap[self.arr[-1]] = self.indexMap[val]
            self.arr[self.indexMap[val]] = self.arr[-1]
            self.arr.pop()
            self.indexMap.pop(val)
            return True
        else:
            return False

    def getRandom(self) -> int:
        return self.arr[randint(0, len(self.arr) - 1)]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()