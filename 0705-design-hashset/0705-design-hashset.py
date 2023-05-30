class MyHashSet:

    def __init__(self):
        self.hashset = [-1 for _ in range(10)]
        self.capacity = 10
        self.no_of_elements = 0

    def makeHashset(self) -> None:
        if self.no_of_elements/self.capacity >= 0.66:
            hashset = self.hashset
            self.hashset = [-1 for _ in range(len(hashset)*2)]
            self.capacity *= 2
            for key in hashset:
                index = key % self.capacity
                if self.hashset[index] == -1:
                    self.hashset[index] = key
                elif self.hashset[index] != key:
                    self.ifCollision(key)

    def ifCollision(self, key: int) -> None:
        index = key % self.capacity
        idx = index
        i = 0
        while self.hashset[idx] > -1 and self.hashset[idx] != key:
            idx = (index + i*i) % self.capacity
            i += 1
        if self.hashset[idx] < 0:
            self.hashset[idx] = key
            self.no_of_elements += 1
    
    def add(self, key: int) -> None:
        index = key % self.capacity
        if self.hashset[index] < 0:
            self.hashset[index] = key
            self.no_of_elements += 1
        elif self.hashset[index] != key:
            self.ifCollision(key)
        self.makeHashset()

    def remove(self, key: int) -> None:
        index = key % self.capacity
        if self.hashset[index] != -1:
            if self.hashset[index] == key: 
                self.hashset[index] = -2
            else:
                idx = index
                i = 0
                while self.hashset[idx] != -1 and self.hashset[idx] != key:
                    idx = (index + i*i) % self.capacity
                    if self.hashset[idx] == key:
                        self.hashset[idx] = -2
                        break
                    i += 1
                        
    def contains(self, key: int) -> bool:
        index = key % self.capacity
        if self.hashset[index] == -1:
            return False
        elif self.hashset[index] == key:
            return True
        idx = index
        i = 0
        while self.hashset[idx] != -1:
            idx = (index + i*i) % self.capacity
            if self.hashset[idx] == key:
                return True
            i += 1
        return False

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)