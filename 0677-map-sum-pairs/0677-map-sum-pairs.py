class MapSum:

    def __init__(self):
        self.dictionary = defaultdict(list)

    def insert(self, key: str, val: int) -> None:
        self.dictionary[key] = val

    def sum(self, prefix: str) -> int:
        total = 0
        for i in self.dictionary:
            if len(prefix) > len(i):
                continue
            flag = True
            for j in range(len(prefix)):
                if prefix[j] != i[j]:
                    flag = False
                if not flag:
                    break
            if flag:
                total += self.dictionary[i]
        return total


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)