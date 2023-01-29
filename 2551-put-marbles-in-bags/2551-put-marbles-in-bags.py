class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        partition = []
        for i in range(len(weights) - 1):
            partition.append(weights[i] + weights[i + 1])
        partition.sort()
        res = 0
        print(partition)
        for i in range(k - 1):
            res += partition[-i - 1] - partition[i]
        return res