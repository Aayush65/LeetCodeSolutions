class Solution:
    def beautySum(self, s: str) -> int:
        total = 0
        index = lambda x: ord(x) - ord('a')
        for i in range(len(s)):
            beauty = [0 for i in range(26)]

            for j in range(i, len(s)):
                mx = -float("inf")
                mn = float("inf")
                beauty[index(s[j])] += 1
                for k in beauty:
                    if k:
                        mx = max(mx, k)
                        mn = min(mn, k)
                total += mx - mn
        return total