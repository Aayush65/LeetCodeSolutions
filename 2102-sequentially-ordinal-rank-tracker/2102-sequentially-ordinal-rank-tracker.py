class SORTracker:

    def __init__(self):
        from sortedcontainers import SortedList
        self.scores = SortedList(key=lambda x: [-x[1], x[0]])
        self.count = -1

    def add(self, name: str, score: int) -> None:
        self.scores.add((name, score))

    def get(self) -> str:
        self.count += 1
        return self.scores[self.count][0]


# Your SORTracker object will be instantiated and called as such:
# obj = SORTracker()
# obj.add(name,score)
# param_2 = obj.get()