class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        memo = {}
        for i in range(n + 1):
            orgI = i
            count = 0
            while i:
                if i in memo:
                    count += memo[i]
                    break
                count += i % 2
                i //= 2
            memo[orgI] = count
            res.append(count)

        return res