class Solution:
    def minWindow(self, s: str, t: str) -> str:
        hashmap = {}
        need = 0
        for i in t:
            if i in hashmap:
                hashmap[i] += 1
            else:
                hashmap[i] = 1
                need += 1
        minStrLen = float("inf")
        res = [0, -1]
        i = j = 0
        while j < len(s):
            while j < len(s) and need:
                if s[j] in hashmap:
                    if hashmap[s[j]] == 1:
                        need -= 1
                    hashmap[s[j]] -= 1
                j += 1
            if need:
                continue
            if len(t) <= j - i < minStrLen:
                res = [i, j - 1]
                minStrLen = j - i
            while i < j and not need:
                if s[i] in hashmap:
                    hashmap[s[i]] += 1
                    if hashmap[s[i]] > 0:
                        need += 1
                i += 1
            if len(t) <= j - i + 1 < minStrLen:
                res = [i - 1, j - 1]
                minStrLen = j - i + 1
        minStr = ''
        for i in range(res[0], res[1]+1):
            minStr += s[i]
        return minStr