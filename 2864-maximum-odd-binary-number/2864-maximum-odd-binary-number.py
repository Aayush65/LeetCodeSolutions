class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        count = 0
        c2 = 0
        for i in s:
            if i == '1':
                count += 1
            else:
                c2 += 1
        res = [] + ['1'] * (count - 1) + ['0'] * c2 + ['1']
        return ''.join(res)        
        