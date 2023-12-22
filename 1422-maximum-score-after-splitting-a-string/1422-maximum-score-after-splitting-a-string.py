class Solution:
    def maxScore(self, s: str) -> int:
        zeroes = []
        total = 0
        for i in s:
            total += (i == '0')
            zeroes.append(total)
        ones = []
        total = 0
        for i in s[::-1]:
            total += (i == '1')
            ones.append(total)
        ones.reverse()
                
        maxScore = 0
        for i in range(len(s) - 1):
            maxScore = max(maxScore, zeroes[i] + ones[i + 1])
        return maxScore