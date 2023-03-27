class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        for i in range(len(s) - 2, -1, -1):
            shifts[i] += shifts[i + 1]
        s = list(s)
        for i in range(len(s)):
            s[i] = chr((ord(s[i]) - ord('a') + shifts[i]) % 26 + ord('a'))
        return ''.join(s)