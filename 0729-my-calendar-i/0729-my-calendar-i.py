class MyCalendar:

    def __init__(self):
        from sortedcontainers import SortedList
        self.time = SortedList([], key = lambda x: x[0])

    def book(self, start: int, end: int) -> bool:
        index = self.time.bisect_right([start])
        if index > 0 and self.time[index - 1][1] > start:
            return False
        if index < len(self.time) and self.time[index][0] < end:
            return False
        self.time.add([start, end])
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)