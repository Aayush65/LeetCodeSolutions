class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        res = {i for i in range(n)}
        for i, j in edges:
            if j in res:
                res.remove(j)
        return res