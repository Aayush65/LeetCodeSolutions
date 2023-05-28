class Solution:
    def minimumCost(self, s: str) -> int:
        n = len(s)
        
        def calcCost(index: int, isLeft: bool, target: int)  -> int:
            cost = 0
            flips = 0
            for i in range(index, -1 if isLeft else n, -1 if isLeft else 1):
                if (s[i] == target and not flips) or (s[i] != target and flips):
                    continue
                flips = (flips + 1) % 2
                cost += i + 1 if isLeft else n - i
            return cost
                    
        if n % 2:
            return min(calcCost(n // 2, True, '1') + calcCost(n // 2 + 1, False, '1'),
                       calcCost(n // 2 - 1, True, '1') + calcCost(n // 2, False, '1'), 
                       calcCost(n // 2, True, '0') + calcCost(n // 2 + 1, False, '0'), 
                       calcCost(n // 2 - 1, True, '0') + calcCost(n // 2, False, '0'))
        return min(calcCost(n // 2, True, '1') + calcCost(n // 2 + 1, False, '1'),
                   calcCost(n // 2, True, '0') + calcCost(n // 2 + 1, False, '0'))