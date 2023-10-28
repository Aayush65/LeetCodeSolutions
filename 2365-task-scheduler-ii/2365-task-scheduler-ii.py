class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        lastDate = {i: -space for i in tasks}
        day = 0
        for i in tasks:
            if day - lastDate[i] >= space:
                day += 1
            else:
                day = space + lastDate[i] + 1
            lastDate[i] = day
        return day