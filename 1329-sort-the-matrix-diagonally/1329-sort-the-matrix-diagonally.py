class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        
        for i in range(m):
            arr = []
            for j in range(n):
                if i + j == m:
                    break
                arr.append(mat[i + j][j])
            arr.sort()
            for j in range(n):
                if i + j == m:
                    break
                mat[i + j][j] = arr[j]
                
        for i in range(n):
            arr = []
            for j in range(m):
                if i + j == n:
                    break
                arr.append(mat[j][i + j])
            arr.sort()
            for j in range(m):
                if i + j == n:
                    break
                mat[j][i + j] = arr[j]
        return mat
        