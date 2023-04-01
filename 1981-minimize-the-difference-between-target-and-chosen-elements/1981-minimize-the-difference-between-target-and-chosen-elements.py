class Solution:
    def minimizeTheDifference(self, mat: List[List[int]], target: int) -> int:
        m = len(mat)
        n = len(mat[0])
        
        @cache
        def dfs(row: int, score: int) -> int:
            if row == len(mat):
                return abs(target - score)
            if score >= target:
                return dfs(row + 1, score + min(mat[row]))
            res = float("inf")
            for i in mat[row]:
                res = min(res, dfs(row + 1, score + i))
            return res
            
        return dfs(0, 0)