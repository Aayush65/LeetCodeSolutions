class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        def rec(index: int) -> int:
            if index == 0:
                return 0
            if rec(index // 2):
                return 0 if index % 2 else 1
            else:
                return 1 if index % 2 else 0

        return rec(k - 1)
