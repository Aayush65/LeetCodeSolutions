class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        diag = set()
        for i in range(len(nums)):
            diag.add(nums[i][i])
            diag.add(nums[i][len(nums) - i - 1])
        
        maxNum = max(diag)
        primes = {i for i in range(2, maxNum + 1)}
        for i in range(2, maxNum + 1):
            if i not in primes:
                continue
            for j in range(i * i, maxNum + 1, i):
                if j in primes:
                    primes.remove(j)
        
        maxPrime = 0
        for i in diag:
            if i in primes:
                maxPrime = max(maxPrime, i)
        return maxPrime