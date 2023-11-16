class MyCalendarTwo:

    def __init__(self):
        from sortedcontainers import SortedList
        self.time = SortedList([], key = lambda x: x[0])

    def book(self, start: int, end: int) -> bool:
        sIdx = self.time.bisect_left([start])
        if sIdx < len(self.time) and self.time[sIdx][0] == start:
            self.time[sIdx][1] += 1
        else:
            self.time.add([start, 1])
        
        eIdx = self.time.bisect_left([end])
        if eIdx < len(self.time) and self.time[eIdx][0] == end:
            self.time[eIdx][1] -= 1
        else:
            self.time.add([end, -1])
        
        total = 0
        toAdd = True
        for i in range(eIdx + 1):
            total += self.time[i][1]
            if total == 3:
                toAdd = False
                break
        
        if toAdd:
            return True
        
        self.time[sIdx][1] -= 1
        if not self.time[sIdx][1]:
            eIdx -= 1
            self.time.pop(sIdx)
        self.time[eIdx][1] += 1
        if not self.time[eIdx][1]:
            self.time.pop(eIdx)
        return False
        
    
# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)