class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        return "".join(list(itertools.permutations([str(i + 1) for i in range(n)], n))[k - 1])