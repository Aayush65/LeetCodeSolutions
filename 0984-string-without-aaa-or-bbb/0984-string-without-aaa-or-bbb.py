class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        chanceOfA = a >= b
        s = []
        while a + b:
            if chanceOfA:
                if a >= b and a > 1:
                    s.append('aa')
                    a -= 1
                else:
                    s.append('a')
                a -= 1
                chanceOfA = False
            else:
                if b >= a and b > 1:
                    s.append('bb')
                    b -= 1
                else:
                    s.append('b')
                b -= 1
                chanceOfA = True
        return ''.join(s)