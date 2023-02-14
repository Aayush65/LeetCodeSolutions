class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(b) > len(a):
            a, b = b, a
        b = '0' * (len(a) - len(b)) + b
        a = a[::-1]
        b = b[::-1]
        i = 0
        res = []
        carry = 0
        while i < len(a):
            res.append(str(int(a[i]) ^ int(b[i]) ^ carry))
            carry = (int(a[i]) & int(b[i])) | (int(a[i]) & carry) | (carry & int(b[i]))
            i += 1
        if carry == 1:
            res.append('1')
                
        return ''.join(res[::-1])