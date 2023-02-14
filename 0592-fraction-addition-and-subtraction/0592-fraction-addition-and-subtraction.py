class Solution:
    def fractionAddition(self, expression: str) -> str:
        def equationHandler(eq):
            newEq = []
            isPos = True
            i = 0
            while i < len(eq):
                if eq[i] == '+':
                    isPos = True
                    i += 1
                elif eq[i] == '-':
                    isPos = False
                    i += 1
                ele = []
                while i < len(eq) and eq[i] not in ['-', '+']:
                    ele.append(eq[i])
                    i += 1
                if ele:
                    newEq.append(''.join(ele) if isPos else ''.join(['-'] + ele))

            fractions = [[],[]]
            for i in newEq:
                div = i.index('/')
                fractions[0].append(int(i[:div]))
                fractions[1].append(int(i[div + 1:]))
            return fractions
        
        fractions = equationHandler(expression)
        denominator = lcm(*fractions[1])

        numerator = 0
        for i in range(len(fractions[0])):
            numerator += fractions[0][i] * (denominator // fractions[1][i])

        if numerator == 0:
            return '0/1'
        hcf = gcd(numerator, denominator)
        numerator //= hcf
        denominator //= hcf

        return str(numerator) + '/' + str(denominator)
