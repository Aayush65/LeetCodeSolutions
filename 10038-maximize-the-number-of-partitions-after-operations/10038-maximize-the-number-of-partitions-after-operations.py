class Solution:
    def maxPartitionsAfterOperations(self, s: str, k: int) -> int:
        
        @cache    
        def dp(index: int, mask: int, changed: bool) -> int:
            if index == len(s):
                return 1
            currBit = 1 << (ord(s[index]) - ord('a'))
            if bin(mask | currBit).count("1") > k:
                res = 1 + dp(index + 1, currBit, changed)
            else:
                res = dp(index + 1, mask | currBit, changed)

            if not changed:
                for i in range(26):
                    newBit = 1 << i
                    if newBit & mask or newBit & currBit:
                        continue
                    newBit = 1 << i
                    newMask = mask | newBit
                    if bin(newMask).count("1") > k:
                        res = max(res, 1 + dp(index + 1, newBit, True))
                    else:
                        res = max(res, dp(index + 1, newMask, True))
            return res


        return dp(0, 0, False)