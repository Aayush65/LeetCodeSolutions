class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0]
        for i in range(1, n + 1):
            count = i % 2 + res[i // 2]
            res.append(count)
        return res