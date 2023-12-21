class Solution:
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        indexOf = lambda x: ord(x) - ord('a')
        freq = [0] * 26
        freqs = [freq.copy()]
        for i in s:
            freq[indexOf(i)] += 1
            freqs.append(freq.copy())
            
        res = []
        for left, right, k in queries:
            resFreq = freqs[right + 1].copy()
            odds = 0
            for i in range(26):
                resFreq[i] -= freqs[left][i]
                if resFreq[i] % 2:
                    odds += 1
            res.append(odds // 2 <= k)            
        return res