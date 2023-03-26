class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        total = 0
        if k < numOnes:
            return k
        else:
            total += numOnes
            k -= numOnes
        if k < numZeros:
            return total
        else:
            k -= numZeros
        if k <= numNegOnes:
            total -= k
            return total            
        return 1