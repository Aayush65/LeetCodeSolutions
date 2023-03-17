class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        s = [0]
        while n and len(s) < k:
            s.append(1)
            s.extend([1 - s[i] for i in range(len(s) - 2, -1, -1)])
        return str(s[k - 1])