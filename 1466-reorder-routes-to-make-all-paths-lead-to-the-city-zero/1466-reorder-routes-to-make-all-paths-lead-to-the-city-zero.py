class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        dt = defaultdict(list)
        for a,b in connections:
            dt[a].append((b,True))
            dt[b].append((a,False))
        ans = 0
        q = [0]
        vis = set()
        while(q):
            node = q.pop()
            vis.add(node)
            for nd,st in dt[node]:
                if nd not in vis:
                    q.append(nd)
                    if st: ans+=1
        return ans