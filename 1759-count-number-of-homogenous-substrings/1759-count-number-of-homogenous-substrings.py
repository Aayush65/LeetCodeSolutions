class Solution:
    def countHomogenous(self, s: str) -> int:
        mod = 1000000007
        i = 0
        homogenous_substrings = 0
        while i < len(s):
            curr = s[i]
            count = 0
            while i < len(s) and curr == s[i]:
                count += 1
                i += 1
            homogenous_substrings += (count * (count + 1) // 2) % mod
        return homogenous_substrings % mod