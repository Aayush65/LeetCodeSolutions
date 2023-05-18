class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        meetings.sort(key = lambda x: [x[2], x[0], x[1]])
            
        partners = {i: [] for i in range(n)}
        for x, y, time in meetings:
            partners[x].append((time, y))
            partners[y].append((time, x))

        secrets = set()
        h = [(0, 0, firstPerson)]
        h.sort()
        while h:
            time, x, y = heappop(h)
            if x not in secrets:
                secrets.add(x)
                for nextTime, nextY in partners[x]:
                    if time <= nextTime:
                        heappush(h, [nextTime, x, nextY])
            if y not in secrets:
                secrets.add(y)
                for nextTime, nextX in partners[y]:
                    if time <= nextTime:
                        heappush(h, [nextTime, y, nextX])
        return secrets