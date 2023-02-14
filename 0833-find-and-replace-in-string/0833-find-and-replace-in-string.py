class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        s = list(s)
        change = [[i, j, k] for i, j, k in zip(indices, sources, targets)]
        change.sort()

        res = []
        i = 0
        j = 0
        while i < len(s):
            while i < len(s) and (j >= len(change) or i < change[j][0]):
                res.append(s[i])
                i += 1
            if j >= len(change):
                continue
            if len(s) - i < len(change[j][1]):
                j += 1
                continue
            toChange = True
            for k in range(len(change[j][1])):
                if s[k + i] != change[j][1][k]:
                    toChange = False
                    break
            if toChange:
                res.append(change[j][2])
                i += len(change[j][1])
            j += 1
        return ''.join(res)