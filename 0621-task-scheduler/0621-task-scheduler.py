class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n == 0:
            return len(tasks)

        count = {i: 0 for i in tasks}
        for i in tasks:
            count[i] += 1
        
        h = []
        for i in count:
            if not i: continue
            heappush(h, -count[i])
        
        currTime = 0
        q = deque()
        while h or q:
            currTime += 1
            if q and q[0][1] == currTime:
                heappush(h, -q.popleft()[0])
            if h:
                leftTasks = -heappop(h)
            else:
                leftTasks, currTime = q.popleft()
            if leftTasks > 1:
                q.append([leftTasks - 1, currTime + n + 1])
        return currTime
            
        
        