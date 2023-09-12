class Solution:
    def minDeletions(self, s: str) -> int:        
        freqMap = {i: 0 for i in s}
        maxFreq = 0
        for i in s:
            freqMap[i] += 1
            maxFreq = max(maxFreq, freqMap[i])
            
        freqs = [0] * (maxFreq + 1)
        for i in freqMap:
            freqs[freqMap[i]] += 1
        
        freqs.reverse()
        freqs.pop()
        carry = 0
        dels = 0
        
        for i in range(len(freqs)):
            freqs[i] += carry
            carry = freqs[i] - 1 if freqs[i] else 0
            dels += carry
            if not freqs[i] and carry:
                carry -= 1
        return dels