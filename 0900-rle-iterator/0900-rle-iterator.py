class RLEIterator:

    def __init__(self, encoding: List[int]):
        self.nums = deque()
        for i in range(0, len(encoding), 2):
            self.nums.append([encoding[i], encoding[i + 1]])

    def next(self, n: int) -> int:
        if not self.nums:
            return -1
        if n > self.nums[0][0]:
            n -= self.nums.popleft()[0]
            return self.next(n)
        self.nums[0][0] -= n
        if self.nums[0][0]:
            return self.nums[0][1]
        return self.nums.popleft()[1]
        


# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(encoding)
# param_1 = obj.next(n)