class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        
        adj = defaultdict(lambda: defaultdict(int))
        change_lengths = set(len(sub) for sub in original)
        
        for i, start in enumerate(original):
            end = changed[i]
            c = cost[i]
            
            if end in adj[start]:
                adj[start][end] = min(adj[start][end], c)
            else:
                adj[start][end] = c
        
        
        allPoints = {x: i for i, x in enumerate(list(set(original + changed)))}
        n = len(allPoints)
        dist = [[float("inf")] * n for _ in range(n)]
        for i in range(n):
            dist[i][i] = 0

        for i, j, val in zip(original, changed, cost):
            i, j = allPoints[i], allPoints[j]
            dist[i][j] = min(dist[i][j], val)

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
        

        @cache
        def dfs(i):
            #let dfs(i) be the cost of matching everything at i and onwards assuming everything before i is matched
            if i >= len(target):
                return 0
            
            c = inf if target[i] != source[i] else dfs(i+1) #if they match save default cost as just continue
            for length in change_lengths:
                t_sub = target[i:i+length]
                s_sub = source[i:i+length]
                trans_cost = inf
                if s_sub in allPoints and t_sub in allPoints:
                    trans_cost = dist[allPoints[s_sub]][allPoints[t_sub]]

                if trans_cost != inf:
                    c = min(c, trans_cost + dfs(i+length))
            return c
        
        ans = dfs(0)
        
        
        return ans if ans != inf else -1