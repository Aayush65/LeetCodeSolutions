class Solution:
    def solveEquation(self, equation: str) -> str:
        equal = equation.index('=')
        lhs = equation[:equal]
        rhs = equation[equal + 1:]

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
            return newEq

        def equationCalculator(eq):
            eq = equationHandler(eq)
            total = 0
            coeff = 0
            for i in eq:
                if i[-1] == 'x':
                    if i[0] == '-' and len(i) == 2:
                        coeff -= 1
                    elif len(i) == 1:
                        coeff += 1
                    else:
                        coeff += int(i[:-1])
                else:
                    total += int(i)
            return (coeff, total)

        lhs = equationCalculator(lhs)
        rhs = equationCalculator(rhs)
        
        if lhs[0] == rhs[0]:
            if lhs[1] == rhs[1]:
                return "Infinite solutions"
            else:
                return "No solution"
        else:
            return 'x=' + str((rhs[1] - lhs[1]) // (lhs[0] - rhs[0]))