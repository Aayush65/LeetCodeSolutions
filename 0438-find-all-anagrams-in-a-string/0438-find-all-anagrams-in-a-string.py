class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []
        hp = {}
        for i in p:
            if i in hp:
                hp[i] += 1
            else:
                hp[i] = 1

        res = []
        for i in range(0, len(p)):
            if s[i] in hp:
                hp[s[i]] -= 1
                if hp[s[i]] == 0:
                    del hp[s[i]]
            else:
                hp[s[i]] = -1
        if len(hp) == 0:
                res.append(0)
        for i in range(len(p), len(s)):
            if s[i] in hp:
                hp[s[i]] -= 1
                if hp[s[i]] == 0:
                    del hp[s[i]]
            else:
                hp[s[i]] = -1

            if s[i - len(p)] in hp:
                hp[s[i - len(p)]] += 1
                if hp[s[i - len(p)]] == 0:
                    del hp[s[i - len(p)]]
            else:
                hp[s[i - len(p)]] = 1
            if len(hp) == 0:
                res.append(i - len(p) + 1)
        return res
