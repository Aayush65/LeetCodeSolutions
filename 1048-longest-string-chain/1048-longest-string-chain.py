class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        n = len(words)

        def isPredecesor(w1: str, w2: str) -> bool:
            if len(w2) != len(w1) + 1:
                return False
            j = 0
            flag = True
            for i in w2:
                if j == len(w1) or w1[j] != i:
                    if not flag:
                        return False
                    flag = False
                else:
                    j += 1
            return not flag

        strMap = {i: [] for i in range(n)}
        for w1 in range(n):
            for w2 in range(n):
                if isPredecesor(words[w1], words[w2]):
                    strMap[w1].append(w2)


        q = [i for i in range(n)]
        steps = 0
        while q:
            steps += 1
            newQ = set()
            for i in q:
                for nei in strMap[i]:
                    newQ.add(nei)
            q = newQ

        return steps