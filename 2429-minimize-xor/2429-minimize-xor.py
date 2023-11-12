class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        bits = bin(num2).count('1')
        zeroes = []
        res = 0
        for i in range(32, -1, -1):
            if num1 & (1 << i):
                res ^= 1 << i
                bits -= 1
            else:
                zeroes.append(i)
            if not bits:
                break
        
        for i in range(bits):
            res |= 1 << zeroes.pop()
        return res