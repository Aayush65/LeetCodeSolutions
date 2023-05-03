class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        par = [i for i in range(n)]
        rank = [1] * n

        def find(n: int) -> int:
            while n != par[n]:
                par[n] = par[par[n]]
                n = par[n]
            return n

        def union(n1: int, n2: int) -> bool:
            p1, p2 = find(n1), find(n2)
            if p2 != n2:
                return False
            if p1 == p2:
                return False
            par[p2] = p1
            rank[p1] += rank[p2]
            rank[p2] = 0
            return True

        for i in range(n):
            if leftChild[i] != -1:
                if not union(i, leftChild[i]):
                    return False
            if rightChild[i] != -1:
                if not union(i, rightChild[i]):
                    return False

        for i in rank:
            if i:
                return i == n