class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        power = [(sum(mat[i]), i) for i in range(len(mat))]
        power.sort()
        res = []
        for i in range(k):
            res.append(power[i][1])
        return res