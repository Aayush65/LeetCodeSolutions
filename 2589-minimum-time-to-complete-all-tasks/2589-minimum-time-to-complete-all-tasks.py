class Solution:
    def findMinimumTime(self, tasks: List[List[int]]) -> int:
        tasks.sort(key = lambda x: x[1])
        time = [0] * 2001
        
        for s, e, d in tasks:
            for i in range(s, e + 1):
                if d == 0:
                    break
                d -= time[i]
            for i in range(e, s - 1, -1):
                if d == 0:
                    break
                if not time[i]:
                    d -= 1
                    time[i] = 1
        return sum(time)
                    