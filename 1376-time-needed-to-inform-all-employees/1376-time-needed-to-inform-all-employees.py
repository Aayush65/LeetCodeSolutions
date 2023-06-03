class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        childNode = [[] for i in range(n)]
        for i in range(len(manager)):
            if manager[i] == -1:
                continue
            childNode[manager[i]].append(i)
        
        print(childNode)
        # return 0
        q = deque([(headID, 0)])
        totalTime = 0
        while q:
            person, time = q.popleft()
            totalTime = max(totalTime, time)
            for child in childNode[person]:
                q.append((child, time + informTime[person]))
        return totalTime