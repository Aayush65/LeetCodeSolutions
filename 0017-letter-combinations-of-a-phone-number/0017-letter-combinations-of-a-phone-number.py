class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        numberLetters = {'2':['a', 'b', 'c'], '3':['d', 'e', 'f'], '4':['g', 'h', 'i'], '5':['j', 'k', 'l'], '6':['m', 'n', 'o'], '7':['p', 'q', 'r', 's'], '8':['t', 'u', 'v'], '9':['w', 'x', 'y', 'z']}
        combs = []

        def allCombs(index: int, combStr: list[str]) -> None:
            if index == len(digits):
                combs.append(''.join(combStr))
                return
            for i in numberLetters[digits[index]]:
                combStr.append(i)
                allCombs(index + 1, combStr)
                combStr.pop()

        if digits:
            allCombs(0, [])

        return combs