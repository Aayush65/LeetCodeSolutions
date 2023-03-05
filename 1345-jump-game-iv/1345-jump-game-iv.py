class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        if n < 2:
            return 0
        
        poss = defaultdict(list)
        for idx, num in enumerate(arr):
            poss[num].append(idx)
        
        bfs, visited, steps = [0], {0}, 0
        while bfs:
            next_bfs = []
            for idx in bfs:
                if idx == n - 1:
                    return steps
                nexts = {
                    i for i in [idx - 1, idx + 1] + poss[arr[idx]]
                    if i >= 0 and i < n and i not in visited
                }
                visited |= nexts
                next_bfs += nexts
                poss[arr[idx]].clear()
            steps += 1
            bfs = next_bfs
        return steps