class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trustMap = {i:set() for i in range(1, n + 1)}
        judges = {i for i in range(1, n + 1)}
        for i, j in trust:
            trustMap[i].add(j)
            if i in judges:
                judges.remove(i)
        if len(judges) != 1:
            return -1
        judge = judges.pop()
        for i in trustMap:
            if i == judge:
                continue
            if judge not in trustMap[i]:
                return -1
        return judge