class Solution:
    def maxValue(self, n: str, x: int) -> str:
        isNegative = n[0] == '-'
        isAppended = False
        res = []
        if isNegative:
            res.append('-')
            n = n[1:]
        for i in n:
            if isNegative:
                if int(i) > x and not isAppended:
                    res.append(str(x))
                    isAppended = True
            else:
                if int(i) < x and not isAppended:
                    res.append(str(x))
                    isAppended = True
            res.append(i)
        if isNegative:
            if len(n) + 1 == len(res):
                res.append(str(x))
        else:
            if len(n) == len(res):
                res.append(str(x))
        return ''.join(res)