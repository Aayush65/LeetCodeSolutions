class Solution:
    def reorganizeString(self, s: str) -> str:
        freqMap = [0] * 26
        indexOf = lambda x: ord(x) - ord('a')
        for i in s:
            freqMap[indexOf(i)] += 1
        
        letters = sorted([[chr(i + ord('a')), freqMap[i]] for i in range(26)], key = lambda x: -x[1])
        newS = [''] * len(s)
        i = 0
        for letter in letters:
            for j in range(letter[1]):
                if i >= len(s):
                    i %= len(s)
                while i == len(s) or newS[i]:
                    i = (i + 1) % len(s)
                newS[i] = letter[0]
                i += 2
        for i in range(1, len(s)):
            if newS[i] == newS[i - 1]:
                return ""
        return ''.join(newS)