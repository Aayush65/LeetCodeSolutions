class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        res = []
        for i in range(len(str(low)), len(str(high)) + 1):
            curr = [j + 1 for j in range(i)]
            for j in range(10 - i):
                currInt = int(''.join([str(k) for k in curr]))
                curr = [k + 1 for k in curr]
                if currInt < low:
                    continue
                if currInt > high:
                    break
                res.append(currInt)
        return res