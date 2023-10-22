class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        s = ['a'] * n
        k -= n
        i = n - 1
        while k:
            if k > 25:
                s[i] = 'z'
                i -= 1
                k -= 25
            else:
                s[i] = chr(ord('a') + k)
                break
        return ''.join(s)