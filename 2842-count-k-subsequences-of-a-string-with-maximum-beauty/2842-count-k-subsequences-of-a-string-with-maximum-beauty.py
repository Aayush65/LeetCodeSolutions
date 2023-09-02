class Solution:
    def countKSubsequencesWithMaxBeauty(self, s: str, k: int) -> int:
        mod = int(1e9 + 7)
        freq = [0] * 26
        indexOf = lambda x: ord(x) - ord('a')
        chars = set()            
    
        for i in s:
            chars.add(i)
            freq[indexOf(i)] += 1
        
        if len(chars) < k:
            return 0
        
        freq.sort(reverse=True)
        config = {}
        base = 1
        for i in range(k):
            if freq[i] not in config:
                config[freq[i]] = 0
            config[freq[i]] += 1
            base *= freq[i]
        
        freqMap = {i: 0 for i in freq}
        for i in freq:
            freqMap[i] += 1
        
        res = base
        for i in config:
            res *= comb(freqMap[i], config[i])
            res %= mod
        return res