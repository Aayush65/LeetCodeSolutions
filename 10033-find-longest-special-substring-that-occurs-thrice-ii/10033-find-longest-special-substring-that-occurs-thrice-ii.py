class Solution:
    def maximumLength(self, s: str) -> int:
        freq = [[] for _ in range(26)]
        indexOf = lambda x: ord(x) - ord('a')
        
        j = 0
        for i in range(len(s)):
            if s[i] != s[j]:
                h = freq[indexOf(s[j])]
                heappush(h, i - j)
                if len(h) > 3:
                    heappop(h)
                j = i
                
        heappush(freq[indexOf(s[j])], i - j + 1)
        if len(freq[indexOf(s[j])]) > 3:
            heappop(freq[indexOf(s[j])])
        
        print(freq)
        maxSize = -1
        for i in range(26):
            size = -1
            freq[i].sort()
            if len(freq[i]) == 1:
                size = freq[i][0] - 2
            elif len(freq[i]) == 2:
                size = max(min(freq[i][0], freq[i][1] - 1), freq[i][1] - 2)
            elif len(freq[i]) == 3:
                size = max(freq[i][0], min(freq[i][1], freq[i][2] - 1), freq[i][2] - 2)
            maxSize = max(maxSize, size)
        return maxSize if maxSize else -1