class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m, n = len(img), len(img[0])
        res = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                total = 0
                count = 0
                for x in range(-1, 2):
                    for y in range(-1, 2):
                        if -1 < i + x < m and -1 < j + y < n:
                            count += 1
                            total += img[i + x][j + y]
                res[i][j] = total // count
        return res