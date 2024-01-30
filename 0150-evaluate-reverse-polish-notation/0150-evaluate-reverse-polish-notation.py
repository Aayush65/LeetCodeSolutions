class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {'+', '-', '*', '/'}
        stack = []
        for i in tokens:
            if i not in operators:
                stack.append(i)
            else:
                b = int(stack.pop())
                a = int(stack.pop())
                if i == '+': stack.append(a + b)
                elif i == '-': stack.append(a - b)
                elif i == '*': stack.append(a * b)
                elif i == '/': stack.append(a / b)
        return int(stack.pop())