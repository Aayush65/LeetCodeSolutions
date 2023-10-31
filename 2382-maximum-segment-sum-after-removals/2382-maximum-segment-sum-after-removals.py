class Solution:
    def maximumSegmentSum(self, nums: List[int], removeQueries: List[int]) -> List[int]:
        
        n = len(nums)
        par = [i for i in range(n)]
        rank = [0] * n
        removeQueries.reverse()
        
        def find(n: int) -> int:
            while n != par[n]:
                par[n] = par[par[n]]
                n = par[n]
            return n
        
        def union(n1: int, n2: int) -> bool:
            p1, p2 = find(n1), find(n2)
            par[p2] = p1
            rank[p1] += rank[p2]
            rank[p2] += rank[p1] - rank[p2]
            return rank[p1]
            
        currMax = 0
        res = []
        for i in removeQueries:
            res.append(currMax)
            rank[i] = nums[i]
            if i > 0 and rank[i - 1]:
                union(i, i - 1)
            if i < n - 1 and rank[i + 1]:
                union(i, i + 1)
            currMax = max(currMax, rank[i])
        res.reverse()
        return res