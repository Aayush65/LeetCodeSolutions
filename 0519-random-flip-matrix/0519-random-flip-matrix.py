class Solution:

    def __init__(self, m: int, n: int):
        self.hm = {}
        self.limit = m * n - 1
        self.m = m
        self.n = n

    def flip(self) -> list[int]:
        rand = randint(0, self.limit)
        if rand in self.hm:
            temp = rand
            rand = self.hm[rand]
            curr = self.limit
            if curr in self.hm:
                curr = self.hm[curr]
            self.hm[temp] = curr
        elif rand != self.limit:
            curr = self.limit
            if curr in self.hm:
                curr = self.hm[curr]
            self.hm[rand] = curr
        self.limit -= 1
        return [rand // self.n, rand % self.n]

    def reset(self) -> None:
        self.limit = self.m * self.n - 1
        self.hm.clear()   

# Your Solution object will be instantiated and called as such:
# obj = Solution(m, n)
# param_1 = obj.flip()
# obj.reset()