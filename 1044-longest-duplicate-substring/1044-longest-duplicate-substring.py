class Solution:
    def longestDupSubstring(self, s: str) -> str:
        p = int(1e9 + 7)
        n = len(s)
        
        indexOf = lambda x: ord(x) - ord('a') + 1
        
        def check(size: int) -> int:
            currHash = 0
            lastPower = 26
            for i in range(size):
                i += 1
                currHash += (indexOf(s[size - i]) * lastPower) % p
                if i < size:
                    lastPower = (lastPower * 26) % p
                currHash %= p
            
            allHash = defaultdict(list)
            allHash[currHash].append([0, size])
            for i in range(size, n):
                currHash -= (indexOf(s[i - size]) * lastPower) % p
                currHash *= 26
                currHash += indexOf(s[i]) * 26
                currHash %= p

                if len(allHash[currHash]):
                    subS = s[i - size + 1: i + 1]
                    for i, j in allHash[currHash]:
                        if subS == s[i: j]:
                            return subS
                allHash[currHash].append([i - size + 1, i + 1])
            return ''
                
        l, r = 0, n - 1
        ans = ''
        while l < r:
            mid = (l + r + 1) // 2
            res = check(mid)
            if res:
                l = mid
                ans = res
            else:
                r = mid - 1
        return ans