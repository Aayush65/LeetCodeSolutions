class Solution:
    def minimumPushes(self, word: str) -> int:
        freq = Counter(list(word))
        freqs = sorted([i for i in freq], key = lambda x: -freq[x])
        print(freqs)
        
        res = 0
        for i in range(len(freqs)):
            res += freq[freqs[i]] * (i // 8 + 1)
        return res