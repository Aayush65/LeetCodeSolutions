class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        m, n = len(mat), len(mat[0])
        k %= n
        for i, row in enumerate(mat):
            if i % 2:
                if row != row[n - k:] + row[:n - k]:
                    return False
            else:
                if row != row[k:] + row[:k]:
                    return False
        return True