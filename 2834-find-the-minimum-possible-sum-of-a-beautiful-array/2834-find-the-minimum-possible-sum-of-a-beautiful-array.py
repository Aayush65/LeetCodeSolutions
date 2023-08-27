class Solution:
    def minimumPossibleSum(self, n: int, k: int) -> int:
        L = min(n, k // 2)
        total = L * (L + 1) // 2
        
        newL = n - L
        if n <= 0:
            return total
        
        bigL = k - 1 + newL
        smallL = k - 1
        
        bigSum = bigL * (bigL + 1) // 2
        smallSum = smallL * (smallL + 1) // 2
        
        total += bigSum - smallSum
        return total