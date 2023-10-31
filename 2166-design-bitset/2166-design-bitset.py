class Bitset:

    def __init__(self, size: int):
        self.bits = [0] * size
        self.n = size
        self.invert = False
        self.total = 0

        
    # invert: Yes, [0,1,1,1,0,0]
    def fix(self, idx: int) -> None:
        if self.invert and self.bits[idx]:
            self.bits[idx] = 0
            self.total += 1
        if not self.invert and not self.bits[idx]:
            self.bits[idx] = 1
            self.total += 1

    def unfix(self, idx: int) -> None:
        if not self.invert and self.bits[idx]:
            self.bits[idx] = 0
            self.total -= 1
        if self.invert and not self.bits[idx]:
            self.bits[idx] = 1
            self.total -= 1

    def flip(self) -> None:
        self.invert = not self.invert
        self.total = self.n - self.total

    def all(self) -> bool:
        return self.total == self.n

    def one(self) -> bool:
        return self.total > 0

    def count(self) -> int:
        return self.total

    def toString(self) -> str:
        if self.invert:
            return ''.join([str(1 - i) for i in self.bits])
        return ''.join([str(i) for i in self.bits])


# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()