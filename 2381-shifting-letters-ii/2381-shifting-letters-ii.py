class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        toShift = [0] * (len(s) + 1)
        for i, j, k in shifts:
            if k:
                toShift[i] += 1
                toShift[j + 1] -= 1
            else:
                toShift[i] -= 1
                toShift[j + 1] += 1
            
        for i in range(1, len(s) + 1):
            toShift[i] += toShift[i - 1]

        s = list(s)
        for i in range(len(s)):
            s[i] = chr((ord(s[i]) - ord('a') + toShift[i]) % 26 + ord('a'))
        return ''.join(s)