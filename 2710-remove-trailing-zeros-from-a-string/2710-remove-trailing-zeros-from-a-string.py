class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        num = list(num)
        while num and num[-1] == '0':
            num.pop()
        return ''.join(num)