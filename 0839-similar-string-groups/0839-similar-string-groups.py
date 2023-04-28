class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        par = [i for i in range(len(strs))]
        rank = [1] * len(strs)
        wordLen = len(strs[0])

        def check(s1: str, s2: str) -> bool:
            count = 0
            for i in range(wordLen):
                if s1[i] != s2[i]:
                    count += 1
                if count > 2:
                    return False
            return True

        def find(n: int) -> int:
            while n != par[n]:
                n = par[n]
            return n

        def union(n1: int, n2: int) -> bool:
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return False
            if rank[p1] >= rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
                rank[p2] = 0
            else:
                par[p1] = p2
                rank[p2] += rank[p1]
                rank[p1] = 0
            return True

        for i in range(len(strs)):
            for j in range(i + 1, len(strs)):
                if check(strs[i], strs[j]):
                    union(i, j)

        groups = 0
        for i in rank:
            if i:
                groups += 1
        print(rank)
        return groups