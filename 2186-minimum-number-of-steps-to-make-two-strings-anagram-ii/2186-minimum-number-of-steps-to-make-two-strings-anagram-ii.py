class Solution:
    def minSteps(self, s: str, t: str) -> int:
        indexOf = lambda x: ord(x) - ord('a')
        
        freq1 = [0] * 26
        freq2 = [0] * 26
        for i in s:
            freq1[indexOf(i)] += 1
        for i in t:
            freq2[indexOf(i)] += 1
        
        res = 0
        for i, j in zip(freq1, freq2):
            if not i and not j:
                continue
            res += abs(i - j)
        return res