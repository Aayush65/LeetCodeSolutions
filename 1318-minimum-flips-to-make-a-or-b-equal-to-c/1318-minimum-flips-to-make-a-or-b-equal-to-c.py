class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        flips = 0
        for i in range(int(log2(max(a, b, c))) + 1):
            bita, bitb, bitc = (a & 2 ** i) >> i, (b & 2 ** i) >> i, (c & 2 ** i) >> i
            if bitc:
                flips += 0 if bita + bitb else 1
            else:
                flips += bita + bitb
        return flips