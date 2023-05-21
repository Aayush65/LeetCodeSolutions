class Solution:
    def punishmentNumber(self, n: int) -> int:
        
        def dp(index: int, score: int) -> bool:
            sq = str(i * i)
            if index == len(sq):
                return i == score
            num = ''
            for j in range(index, len(sq)):
                num += sq[j]
                if dp(j + 1, score + int(num)):
                    return True            
            return False
        
        total = 0
        for i in range(1, n + 1):
            if dp(0, 0):
                total += i * i
        return total