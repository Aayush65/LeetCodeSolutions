class Solution:
    def minimumSteps(self, s: str) -> int:
        zeroes = []
        for i, x in enumerate(s):
            if x == '0':
                zeroes.append(i)
        
        left = 0
        swaps = 0
        for i in zeroes:
            swaps += i - left
            left += 1
        return swaps