class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        xors = [0]
        for i in arr:
            xors.append(xors[-1] ^ i)
        
        res = []
        for i, j in queries:
            res.append(xors[j + 1] ^ xors[i])
        return res