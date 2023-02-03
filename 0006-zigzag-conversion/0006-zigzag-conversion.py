class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        mat = [[] for _ in range(numRows)]
        j = 0
        goingDown = True 
        for i in s:
            mat[j].append(i)
            if j == numRows - 1 and goingDown == True:
                goingDown = False
            elif j == 0 and goingDown == False:
                goingDown = True
            if goingDown:
                j += 1
            else:
                j -= 1
        res = []
        for i in mat:
            for j in i:
                res.append(j)
        return ''.join(res)