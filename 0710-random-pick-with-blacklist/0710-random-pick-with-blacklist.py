class Solution:

    def __init__(self, n: int, blacklist: list[int]):
        self.hm = {}
        n -= 1
        for i in blacklist:
            curr = n
            while curr in self.hm:
                curr = self.hm[curr]
            self.hm[i] = curr
            if n in self.hm:
                del self.hm[n]
            n -= 1
        self.n = n

    def pick(self) -> int:
        rand = randint(0, self.n)
        while rand in self.hm:
            rand = self.hm[rand]
        return rand

# Your Solution object will be instantiated and called as such:
# obj = Solution(n, blacklist)
# param_1 = obj.pick()