class LUPrefix:

    def __init__(self, n: int):
        self.videos = [0] * n
        self.n = n
        self.prefix = 0

    def upload(self, video: int) -> None:
        self.videos[video - 1] = 1
        while self.prefix < self.n and self.videos[self.prefix]:
            self.prefix += 1

    def longest(self) -> int:
        return self.prefix


# Your LUPrefix object will be instantiated and called as such:
# obj = LUPrefix(n)
# obj.upload(video)
# param_2 = obj.longest()