class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        rows = [sum(i) for i in mat]
        cols = []
        for i in range(len(mat[0])):
            total = 0
            for j in range(len(mat)):
                total += mat[j][i]
            cols.append(total)
            
        count = 0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if rows[i] == 1 and cols[j] == 1 and mat[i][j] == 1:
                    count += 1
        return count