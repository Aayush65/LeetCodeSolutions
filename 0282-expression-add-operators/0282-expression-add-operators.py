class Solution:
    def addOperators(self, num: str, target: int) -> List[str]: 
#         allCombinations = []

#         def isLeadingZero(exp: str):
#             total = 0
#             for i in exp[::-1]:
#                 if i in {"*", "+", "-"}:
#                     break
#                 total += int(i)
#             return total == 0

#         def backtrack(index: int, exp: str) -> None:
#             if index == len(num):
#                 if eval(exp)== target:
#                     allCombinations.append(exp)
#                 return

#             leadingZero = isLeadingZero(exp)
#             for i in ['*', '+', '-', '']:
#                 if not leadingZero or i:
#                     backtrack(index + 1, exp + i + num[index])

#         backtrack(1, num[0])
#         return allCombinations
        allCombinations = []
    
        def backtracking(index: int, exp: str):
            if index == len(num):
                if eval(exp) == target:
                    allCombinations.append(exp)
                return 

            operand = ''
            for i in range(index, len(num)):
                operand += num[i]
                backtracking(i + 1, exp + '*' + operand)
                backtracking(i + 1, exp + '+' + operand)
                backtracking(i + 1, exp + '-' + operand)
                if operand == '0':
                    break

        firstOperand = ''
        for i in range(len(num)):
            firstOperand += num[i]
            backtracking(i + 1, firstOperand) 
            if firstOperand == '0':
                break
        return allCombinations